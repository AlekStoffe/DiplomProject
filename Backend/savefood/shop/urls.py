from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('company/create/', views.CompanyCreateView.as_view()),
    path('food/create/', views.FoodCreateView.as_view()),
    path('map/', views.CompanyMapView.as_view()),
    path('main/', views.FoodMainListView.as_view()),
    path('filters/', views.FoodFilterListView.as_view()),
    path('company/', views.СompanyListView.as_view()),
    path('company/name/', views.CompanyInfoView.as_view()),
]