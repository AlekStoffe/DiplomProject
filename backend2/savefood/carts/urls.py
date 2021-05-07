from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view()),#url = /cart    post={"food": id} / put {"id": CartItems.id} / delete {"id": CartItems.id}
    path('cart/<int:company>', views.CartView.as_view()),   #url = /cart/номер компании, например выглядит как cart/1
    path('cart/confirmation/', views.CartConfirm.as_view()), #подтверждение корзины url = /cart/comfirmation/номер компании например выглядит как cart/confirmation/1
    path('cart/delete/', views.CartDelete.as_view()),

    path('order/me/', views.UserOrderConfirm.as_view()), #заказы пользователя url = /order/me/
    path('order/me/id/', views.OrderUserView.as_view()),#вывод подтвержденных корзин для пользователя

    path('company/order/', views.СompanyOrderConfirm.as_view()), #заказы компании ?company=
    path('company/order/id/', views.OrderCompanyView.as_view()),#вывод подтвержденных корзин для компаний

    path('company/order/cancel/', views.OrderCancelCompanyView.as_view()),#отмена корзины компанией
    path('company/order/confirm/', views.OrderAcceptCompanyView.as_view()),#подтверждение
]