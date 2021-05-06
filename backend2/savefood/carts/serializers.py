from rest_framework import serializers
from . import models
from shop.serializers import FoodCartSerializers

class CartSerialezers(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'

class CartItemSerialezers(serializers.ModelSerializer):
    cart = CartSerialezers()
    food = FoodCartSerializers()
    class Meta:
        model = models.CartItem
        fields = '__all__'