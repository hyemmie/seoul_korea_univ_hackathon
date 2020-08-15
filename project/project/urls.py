"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', views.start, name='start'),
    path('index', views.index, name="index"),

    path('registration/check', views.check, name='check'),
    path('registration/signup', views.signup, name='signup'),
    path('registration/setnickname', views.setnickname, name='setnickname'),
    path('registration/login', views.login, name='login'),
    path('registration/logout', views.logout, name='logout'),


    path('mypage', views.mypage, name='mypage'),
    path('mypage/editmyprofile',
         views.editmyprofile, name="editmyprofile"),
    path('mypage/certificationlocation',
         views.certificationlocation, name="certificationlocation"),
    path('mypage/certificationbuilding',
         views.certificationbuilding, name="certificationbuilding"),

    path('affiliate', views.affiliate, name="affiliate"),
    path('affiliate_detail', views.affiliate_detail, name="affiliate_detail"),

    path('building', views.building, name="building"),
    path('info', views.info, name="info"),
    path('share', views.share, name="share"),
    path('sale', views.sale, name="sale"),
    path('talk', views.talk, name="talk"),

]
