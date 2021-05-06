from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotFound
import django_filters.rest_framework
from .serializers import *
from . import models
# Create your views here.


class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        cart = models.Cart.objects.filter(user=user, order=False).first()
        queryset = models.CartItem.objects.filter(cart=cart)
        serializer = CartItemSerialezers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        cart_user = models.Cart.objects.filter(user=user).values()
        food = models.Food.objects.get(id=data.get('food'))

        # проверка есть ли карта у пользователя, если нет, создание карты
        if cart_user.count() == 0:
            cart_user = models.Cart(user=user, order=False)
            cart_user.save()

        cart = models.Cart.objects.get(user=user, order=False)
        # проверка на входимость
        c_i = models.CartItem.objects.filter(user=user, cart=cart.id, food=food.pk).values()
        if not c_i.count():
            cart_items = models.CartItem(cart=cart, user=user, food=food, price=food.price, quantity=1)
            cart_items.save()
            total_price = 0
            cart_items = models.CartItem.objects.filter(user=user, cart=cart.id)
            for items in cart_items:
                total_price += items.price
            cart.total_price = total_price
            cart.save()
            return Response({'success': 'Вы добавили товар в корзину'})
        else:
            return Response({'success': 'Товар уже добавлен в корзину'})

    def put(self, request):
        data = request.data
        cart_item = models.CartItem.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Товар обновлен'})

    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = models.CartItem.objects.get(id=data.get('id'))
        cart_item.delete()
        cart = models.Cart.objects.filter(user=user, order=False).first()
        queryset = models.CartItem.objects.filter(cart=cart)
        serializer = CartItemSerialezers(queryset, many=True)
        return Response(serializer.data)
