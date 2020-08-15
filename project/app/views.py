from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
# Create your views here.


def main(request):
    return render(request, 'startPage/start.html')


def logout(request):
    auth.logout(request)
    return redirect('main')
