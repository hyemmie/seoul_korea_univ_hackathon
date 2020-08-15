from django.shortcuts import render, redirect
from building.models import Building, Review, BuildingScore
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.
def map(request):
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

        # 0~5를 벗어난 범위의 점수를 입력하면 에러 발생
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


@csrf_exempt
def matching(request):
    request_body = json.loads(request.body)
    print(request.body)
    building_loc = request_body['location']
    loc_latitude = request_body['latitude']
    loc_longitude = request_body['longitude']
    try:
        building_already = Building.objects.get(location_str = building_loc)
    except:
        Building.objects.create(
            location_str = building_loc, score = 0, loc_latitude = loc_latitude, loc_longitude = loc_longitude
        )
    
    response = {
        "bid": building_already.id,
    }
    return HttpResponse(json.dumps(response))



    # def like(request):
    # if request.method == "POST":
    #     request_body = json.loads(request.body)
    #     post_pk = request_body['post_pk']
    #     existing_like = Like.objects.filter(
    #         post=Post.objects.get(pk= post_pk ),
    #         user=request.user
    #     )
    #     if existing_like.count() > 0:
    #         existing_like.delete()
    #     else:
    #         Like.objects.create(
    #             post=Post.objects.get(pk=post_pk),
    #             user=request.user
    #         )   
    #     post_likes = Like.objects.filter(
    #         post=Post.objects.get(pk=post_pk)
    #     )
    #     check = Like.objects.filter(
    #         post=Post.objects.get(pk= post_pk ),
    #         user=request.user
    #     )
    #     response = {
    #         'like_count': post_likes.count(),
    #         'check' : check.count()
    #     }
    #     return HttpResponse(json.dumps(response))