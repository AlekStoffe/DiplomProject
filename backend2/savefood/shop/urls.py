from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('main/1', views.FoodListView1.as_view()),    #вывод мейн страницы
    path('main/2', views.FoodListView2.as_view()),    #
    path('main/3', views.FoodListView3.as_view()),    #

    path('company/', views.CompanyInfoView.as_view()),  #поиск информации о компании по id (company/?id=) или вывод всех компаний
    path('company/user/', views.CompanyUserView.as_view()), #поиск компаний по юзеру(user=id)
    path('company/<int:pk>', views.CompanyDetailView.as_view()), #редактирование/удаление компаний
    path('company/create/', views.CompanyCreateView.as_view()), #создание компании
    path('company/map/', views.CompanyMapView.as_view()),  #вывод на карту
    path('company/map/search/', views.CompanyNameView.as_view()), #поиск по названию на карте

    path('food/', views.FoodFilterListView.as_view()),  #вывод всей еды или поиск по фильтру типа еды
    path('food/create/', views.FoodCreateView.as_view()), #создание еды
    path('food/<int:pk>/', views.FoodDetailView.as_view()), #редактирование/удаление еды

    path('user/telephone/', views.TelephoneUserView.as_view()), #добавление телефона
    path('user/telephone/<int:pk>', views.TelephoneDetailView.as_view()), #удаление/обновление телефона
    path('user/info/', views.UserInfoView.as_view()),#поиск инфы о пользователи по id (?id=)

    path('comment/create/', views.ReviewCreateView.as_view()), #создание комента
    path('company/comment/', views.CompanyReviewList.as_view()), #вывод коментариев компании(чтобы их получить надо в теле пост запроса отправить id компании)
    path('comment/delete/', views.ReviewDelete().as_view()),#удаление коментариев компании(чтобы удалить надо в теле пост запроса отправить id комментария)
    path('company/avgscore/', views.ReviewAvgScoreCompany.as_view())#вывод средней оценки  компании(чтобы его получить надо в теле пост запроса отправить id компании)
]