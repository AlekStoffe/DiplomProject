from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import generics
import django_filters.rest_framework
from shop.models import Food
from django.core import serializers as core_serializers
from .serializers import *
from . import models
# Create your views here.


class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, company):
        user = request.user
        cart = models.Cart.objects.filter(user=user, order=False, company=company).first()
        queryset = models.CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        food = models.Food.objects.get(id=data.get('food'))

        #получааем все карты по фильту
        cart_user = models.Cart.objects.filter(user=user, order=False, company=food.company)
        # проверка есть ли карта у пользователя, если нет, создание карты
        if cart_user.count() == 0:
            cart_user = models.Cart(user=user, company=food.company)
            cart_user.save()

        cart = models.Cart.objects.get(user=user, company=food.company, order=False)

        #получаем карты с компаниями не отн. к нашему типу компаний
        cart_company = models.Cart.objects.filter(user=user).exclude(company=food.company, order=True)

        # проверка на корзину магазина
        if cart_company.count() == 0:
            cart_items = models.CartItem(cart=cart, user=user, food=food, price=food.price, quantity=1)
            cart_items.save()
            total_price = 0
            cart_items = models.CartItem.objects.filter(user=user, cart=cart.id)
            for items in cart_items:
                total_price += items.price
            cart.total_price = total_price
            cart.save()
            return Response({'success': 'Корзина была очищена'})

        # проверка на входимость
        c_i = models.CartItem.objects.filter(user=user, cart=cart.id, food=food.pk)
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
        user = request.user
        cart_item = models.CartItem.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()

        if cart_item.quantity <= 0:
            cart_item.delete()

        cart = models.Cart.objects.get(user=user, order=False)
        cart_items = models.CartItem.objects.filter(user=user, cart=cart.id)
        total_price = 0

        for items in cart_items:
            total_price += items.price

        cart.total_price = total_price
        cart.save()

        return Response({'success': 'Товар обновлен'})

#удаление корзины
class CartDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        data = request.data
        cart = models.Cart.objects.get(id=data.get('id'))
        cart.delete()
        return Response({'success': 'Корзина была удалена'})


#Подтверждение корзины
class CartConfirm(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user
        data= request.data
        cart = models.Cart.objects.filter(user=user, order=False, company=data.get('company')).first()

        if not cart:
            return Response({"success": "Добавьте товар в корзину"})

        cart_items = models.CartItem.objects.filter(cart=cart.id)

        if not cart_items.count():
            return Response({'success': 'Добавьте товар в корзину'})
        else:
            cart.order = True
            models.CartItem.objects.filter(cart=cart).update(items_order=True)
            cart.save()
            return Response({'success': 'Заказ подтвержден'})


#вывод подтвержденных корзин для юзера
class UserOrderConfirm(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Cart.objects.filter(order=True)
    serializer_class = CartSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ['user']


#вывод подтвержденных корзин для компании
class СompanyOrderConfirm(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Cart.objects.filter(order=True)
    serializer_class = CartSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ['company',]


#вывод подтвержденных корзина итемсов для юзера
class OrderUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user
        data = request.data
        cart = models.Cart.objects.filter(user=user, order=True, pk=data.get('id')).first()
        queryset = models.CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializers(queryset, many=True)
        return Response(serializer.data)


#вывод подтвержденных корзина итемсов для компании
class OrderCompanyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        data = request.data
        cart = models.Cart.objects.filter(order=True, pk=data.get('id')).first()
        queryset = models.CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializers(queryset, many=True)
        return Response(serializer.data)

class OrderCancelCompanyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        data = request.data
        cart = models.Cart.objects.filter(order=True, pk=data.get('id'))
        cart.delete()
        return Response({'success': 'Заказ отменен'})

class OrderAcceptCompanyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        data = request.data
        for i in range(len(data)):
            food = Food.objects.get(id=data[i]['id'])
            quant = food.quantity - data[i]['quantity']
            if quant <= 0:
                food.delete()
            else:
                food.quantity = quant
                food.save()
        cart = models.Cart.objects.get(id=data[0]['cart'])
        cart.delete()


