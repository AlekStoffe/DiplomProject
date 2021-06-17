from rest_framework import serializers
from . import models
from django.contrib.auth.models import User



#компания
class CompanyDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

#Карта компаний
class CompanyMapSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'address', 'lat', 'lon', 'id')

#Компании юзера
class CompanyUserDetatilSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'company_type', 'id')


#Название компаний для вывода еды
class CompanyNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name', 'id')

#Еда
class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'

class FoodSerializersList(serializers.ModelSerializer):
    company = CompanyNameSerializers()
    class Meta:
        model = models.Food
        fields = '__all__'

class FoodIdserializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ('pk',)

#Еда для корзины
class FoodCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ('name',  'price', 'quantity', 'company', 'id')


#Вывод информации о компании с едой
class CompanyInfoSerializers(serializers.ModelSerializer):
    food = FoodSerializers(source='company', many=True, read_only=True)
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'description', 'address', 'food')



#телефон
class TelephoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    profile = TelephoneSerializers()
    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name', 'profile')

class UserInfoTrashSerializers(serializers.ModelSerializer):
    profile = TelephoneSerializers()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'profile')

class UserNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ReviewSerializers(serializers.ModelSerializer):
    user = UserNameSerializers()
    class Meta:
        model = models.Review
        fields = '__all__'

