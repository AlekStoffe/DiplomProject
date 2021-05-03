from django.shortcuts import render
from rest_framework import generics
import django_filters.rest_framework
from . import serializers
from . import models
#Создание компании
class CompanyCreateView(generics.CreateAPIView):
    serializer_class = serializers.CompanyDetailSerializers

class CompanyUpdateView(generics.UpdateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanyDetailSerializers


#Создание еды
class FoodCreateView(generics.CreateAPIView):
    serializer_class = serializers.FoodDetailSerializers


#Вывод инфы о компаниях на мапу
class CompanyMapView(generics.ListAPIView):
    queryset = models.Company.objects.exclude(lat=0.0).exclude(lon=0.0)
    serializer_class = serializers.CompanyMapSerializers


#вывод инфы о компании c едой
class CompanyInfoView(generics.ListAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanyInfoSerilizers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ['id']

#вывод листа компаний
class СompanyListView(generics.ListAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanyListSerializers


#Вывод по типам еды
class FoodFilterListView(generics.ListAPIView):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ['food_type']


#вывод на мейн страницу
class FoodMainListView(generics.ListAPIView):
    queryset = list(models.Food.objects.filter(food_type='1'))[:-6:-1] + list(models.Food.objects.filter(food_type='2'))[:-6:-1] + list(models.Food.objects.filter(food_type='3'))[:-6:-1]
    serializer_class = serializers.FoodSerializers

