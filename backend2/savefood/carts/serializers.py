from rest_framework import serializers
from . import models
from shop.serializers import FoodCartSerializers

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'

class CartItemSerializers(serializers.ModelSerializer):
    #cart = CartSerializers()
    food = FoodCartSerializers()
    class Meta:
        model = models.CartItem
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ('user', 'company', 'order', 'total_price', 'pk')

