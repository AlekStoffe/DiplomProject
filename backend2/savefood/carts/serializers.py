from rest_framework import serializers
from . import models
from shop.serializers import FoodSerializersList, CompanyNameSerializers, FoodIdserializers

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'

class CartItemSerializers(serializers.ModelSerializer):
    #cart = CartSerializers()
    food = FoodSerializersList()
    class Meta:
        model = models.CartItem
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    company = CompanyNameSerializers()
    class Meta:
        model = models.Cart
        fields = ('user', 'company', 'order', 'total_price', 'pk', 'company')

