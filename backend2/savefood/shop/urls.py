from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.FoodMainListView.as_view()),    #Вывод мейн страницы
    path('company/', views.СompanyListView.as_view()),  # вывод всех компаний
    path('company/create/', views.CompanyCreateView.as_view()), # создание компании
    #path('company/update/<str:id>', views.CompanyUpdateView.as_view()), #обновление инфы
    path('company/id/', views.CompanyInfoView.as_view()),  # поиск информации о компании по названием
    path('company/map/', views.CompanyMapView.as_view()),  # вывод на карту
    path('food/create/', views.FoodCreateView.as_view()), # cоздание еды
    path('food/', views.FoodFilterListView.as_view()),  # вывод всей еды или поиск по фильтру типа еды

]