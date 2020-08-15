from django.contrib import admin
from django.urls import path, include
from building import views

urlpatterns = [
    path('', views.map, name='map'),
    path('map/', views.map, name='map'),
    path('matching/', views.matching, name='matching'),
    path('<int:id>/', views.building_info, name='building_info'),
    path('<int:id>/evaluate/', views.evaluate, name='building_evaluate'),
]