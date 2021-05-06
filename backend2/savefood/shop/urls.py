from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('main/1', views.FoodListView1.as_view()),    #вывод мейн страницы
    path('main/2', views.FoodListView2.as_view()),    #
    path('main/3', views.FoodListView1.as_view()),    #

    path('company/', views.CompanyInfoView.as_view()),  #поиск информации о компании по id (company/?id=) или вывод всех компаний
    path('company/<int:pk>', views.CompanyDetailView.as_view()), #редактирование/удаление компаний
    path('company/create/', views.CompanyCreateView.as_view()), #создание компании
    path('company/map/', views.CompanyMapView.as_view()),  #вывод на карту

    path('food/', views.FoodFilterListView.as_view()),  #вывод всей еды или поиск по фильтру типа еды
    path('food/create/', views.FoodCreateView.as_view()), #создание еды
    path('food/<int:pk>/', views.FoodDetailView.as_view()), #редактирование/удаление еды

    path('user/telephone/', views.TelephoneUserView.as_view()), #добавление телефона
    path('user/telephone/<int:pk>', views.TelephoneDetailView.as_view()), #удаление/обновление телефона

]