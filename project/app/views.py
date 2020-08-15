from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .models import Profile
# Create your views here.


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


def affiliate(request):
    return render(request, 'affiliate.html')

def affiliate_detail(request):
    return render(request, 'affiliate_detail.html')

def building(request):
    return render(request, 'building.html')

def info(request):
    return render(request, 'info.html')

def share(request):
    return render(request, 'share.html')
def share_detail(request):
    return render(request, 'share_detail.html')



def talk(request):
    return render(request, 'talk.html')
