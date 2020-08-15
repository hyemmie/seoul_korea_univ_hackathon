from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Profile, Rental, Comment
from time import gmtime, strftime
import json
from .models import Profile
# Create your views here.

def home(request):
    posts= Rental.objects.all().order_by('deadline')
    return render(request,'home.html',{'posts':posts})

def start(request):
    return render(request, 'registration/start.html')


def check(request):
    if request.user.username:
        return redirect('index')
    return render(request, 'registration/check.html')


@login_required(login_url='registration/check')
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if found_user:
            error = '해당 아이디는 이미 존재합니다.'
            return render(request, 'registration/signup.html', {'error': error})

        newUser = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, newUser,
                   backend='django.contrib.auth.backends.ModelBackend')
        return redirect('setnickname')
    return render(request, 'registration/signup.html')


@login_required(login_url='registration/signup')
def setnickname(request):
    if request.method == 'POST':
        foundNickname = Profile.objects.filter(
            nickname=request.POST['nickname'])
        if len(foundNickname):
            error = "해당 닉네임은 이미 존재합니다."
            return render(request, 'registration/setnickname.html', {'error': error})
        newProfile = Profile(
            username=request.user,
            nickname=request.POST['nickname']
        )
        newProfile.save()
        return redirect('index')

    return render(request, 'registration/setnickname.html')


def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if found_user is None:
            error = 'id 또는 패스워드가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next', '/index'))
    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('start')


def count(y_m_d):
    time = strftime("%Y-%m-%d", gmtime()).split('-')
    b = int(time[0])*365 + int(time[1])*30 +int(time[2])
    a = int(y_m_d[0])*365 + int(y_m_d[1])*30 + int(y_m_d[2])
    print(a, "데드라인 날짜로 변환")
    print(b, "지금 날짜")
    if a>b:
        result = f"마감 {a-b}일 임박!!"
    else:
        result = "마감일이 지난 나눔입니다."
    return result

# @login_required(login_url = '/registration/login')
def new(request):
    if request.method=='POST':
        print(request.user)
        y_m_d = (request.POST['deadline'].split('-')) 
        new_post= Rental.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            region=request.user.profile.region,
            author = request.user.username,
            deadline = request.POST['deadline'],
            left = count(y_m_d),
        )
         
     
        return redirect('detail',post_pk=new_post.pk)
    else:
        return render(request,'new.html')

def detail(request, post_pk):
    chosen_post= Rental.objects.get(pk= post_pk)
    posts= Rental.objects.all()
    if request.method=="POST":
        Comment.objects.create(
            post = chosen_post,
            content = request.POST['content'],
            author= request.user.username
        )
        return redirect('detail', post_pk)
    return render (request, 'detail.html',{'chosen_post':chosen_post, 'posts':posts})

def delete_comment(request, post_pk, comment_pk):
    comment= Comment.objects.get(pk= comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def edit_comment(request, post_pk, comment_pk ):
    comment= Comment.objects.get(pk = comment_pk)
    if request.method=='POST':
        Comment.objects.filter(pk= comment_pk).update(
         content= request.POST['content'],
         author= request.user.username
        )
        return redirect ('detail',post_pk)
    return render(request, 'edit_comment.html')

def delete(request, post_pk):
    chosen_post= Rental.objects.get(pk= post_pk)
    chosen_post.delete()
    return redirect ('home')

def edit(request, post_pk):
    chosen_post = Rental.objects.get(pk= post_pk)
    if request.method == 'POST':
        y_m_d = (request.POST['deadline'].split('-'))
        Rental.objects.filter(pk= post_pk).update(
         title=request.POST['title'],
         content=request.POST['content'],
         region=request.user.profile.region,
         author = request.user.username,
         deadline = request.POST['deadline'],
         left = count(y_m_d),
        )
        return redirect('detail', post_pk)
    return render(request, 'edit.html', {'chosen_post': chosen_post})

@login_required(login_url='registration/check')
def mypage(request):
    return render(request, 'myPage/mypage.html')


@login_required(login_url='registration/check')
def editmyprofile(request):
    return render(request, 'myPage/editmyprofile')


@login_required(login_url='registration/check')
def certificationlocation(request):
    if(request.method == 'POST'):

        currentProfile = Profile.objects.filter(pk=request.user.pk)
        currentProfile.update(region=request.POST['region'])
        messages = "정상적으로 위치를 설정했습니다."
        return render(request, 'myPage/mypage.html', {'messages': messages})
    return render(request, 'myPage/certificationlocation.html')


@login_required(login_url='registration/check')
def certificationbuilding(request):
    return render(request, 'myPage/editmyprofile')