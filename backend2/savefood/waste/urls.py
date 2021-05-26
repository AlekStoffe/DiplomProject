from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('trash/create/', views.TrashCreateView.as_view()),
    path('trash/', views.TrashListView.as_view()),
    path('trash/info/', views.TrashIdView.as_view()),

]