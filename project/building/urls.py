from django.contrib import admin
from django.urls import path, include
from building import views

urlpatterns = [
    path('map/', views.map, name='map'),
]