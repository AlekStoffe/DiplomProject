from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view()),#url = /cart    post={"food": id} / put {"id": CartItems.id} / delete {"id": CartItems.id}
    path('cart/<int:company>', views.CartView.as_view()),   #url = /cart/номер компании, например выглядит как cart/1
    path('cart/confirmation/<int:company>', views.CartConfirm.as_view()), #подтверждение корзины url = /cart/comfirmation/номер компании например выглядит как cart/confirmation/1
    path('order/me/', views.UserOrderConfirm.as_view()), #заказы пользователя url = /order/me/
    path('company/order/', views.СompanyOrderConfirm.as_view()), #заказы компании ?company=
    path('order/me/<int:pk>', views.OrderUserView.as_view()),#вывод подтвержденных корзин для пользователя
    path('company/order/<int:pk>', views.OrderCompanyView.as_view()),#вывод подтвержденных корзин для компаний
    path('company/order/cancel/<int:pk>', views.OrderCancelCompanyView.as_view()),
]