from django.shortcuts import render, redirect
from building.models import Building, Review, BuildingScore

# Create your views here.
def map(request):
    print('map 왔음')
    return render(request, 'building/map.html')


def building_info(request, id):
    building = Building.objects.get(id=id)
    reviews = Review.objects.filter(building=id) 
    return render(request, 'building/building_info.html', {'building': building, 'reviews': reviews})


def evaluate(request, id):
    building = Building.objects.get(id=id)
    if request.method == "POST":
        content = request.POST['review-content']
        score = request.POST['review-score']

        if (int(score) > 5) or (int(score) < 0):
            error = '0~5 사이의 점수를 입력해주세요!'
            return render(request, 'building/evaluate.html', {'building': building, 'error': error})

        # 우선 리뷰를 만들고
        Review.objects.create(
            user = request.user, building = building, content = content
        )

        # 건물 평점을 업데이트
        # 1. 건물 평점 모델을 생성하고
        BuildingScore.objects.create(
            building = building, evaluated_by = request.user, score = score
        )
        # 2. 건물 평점 모델 중 해당 건물과 관련된 평점의 갯수를 받아서
        score_lists = BuildingScore.objects.all().filter(building = building)
        cnt = score_lists.count()
        score_sum = 0

        # 3. 평점 평균 계산하고 평점 업데이트
        for score in score_lists:
            score_sum += score.score
        score_avg = round((score_sum / cnt), 1)
        
        building.score = score_avg
        building.save()
        return redirect('/building/' + str(id))
    return render(request, 'building/evaluate.html', {'building': building}) 