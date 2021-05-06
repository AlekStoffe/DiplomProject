from rest_framework import serializers
from . import models

#---------------------Сериализаторы компаний--------------------------#

#Создание компании
class CompanyDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

#Карта компаний
class CompanyMapSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'description', 'address', 'lat', 'lon', 'id')





#Еда
class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'


#Еда для корзины
class FoodCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ('name',  'price')


#Вывод информации о компании с едой
class CompanyInfoSerilizers(serializers.ModelSerializer):
    food = FoodSerializers(source='company', many=True, read_only=True)
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'description', 'address', 'food')



#Добавление телефона к пользователю
class TelephoneSerilizers(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'


