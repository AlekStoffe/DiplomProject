from rest_framework import serializers
from . import models
#Создание компании
class CompanyDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

#Карта
class CompanyMapSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'description', 'address', 'lat', 'lon',)

#Лист компаний
class CompanyListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'description', 'address')
#Еда
class FoodDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'

#Вывод инфы о еде
class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ('name', 'image', 'description', 'price', 'quantity', 'food_type', 'company')


#Вывод информации о компании с едой
class CompanyInfoSerilizers(serializers.ModelSerializer):
    food = FoodSerializers(source='company', many=True, read_only=True)
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'description', 'address', 'food')

