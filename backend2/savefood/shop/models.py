from django.db import models
from  django.contrib.auth  import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
Users = get_user_model()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(verbose_name='Телефон:', max_length=11)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



#Модель компании
class Company(models.Model):
    name = models.CharField(verbose_name='Название:', max_length=128, unique=True)
    email = models.EmailField(verbose_name='Почта', blank=True)
    description = models.TextField(verbose_name='Описание:', blank=True)
    image = models.ImageField(verbose_name='Фото:', upload_to='images')
    telephone = models.CharField(verbose_name='Телефон:', max_length=11)
    address = models.CharField(verbose_name='Адрес:', max_length=128, blank=True)
    lat = models.FloatField(verbose_name='Широта:', blank=True)
    lon = models.FloatField(verbose_name='Долгота:', blank=True)
    COMPANY_TYPES = (
        (1, 'Кафе/кофейня/бар'),
        (2, 'Ресторан'),
        (3, 'Столовая'),
        (4, 'Гостиница'),
        (5, 'Местный производитель'),
        (6, 'Местный фермер'),
        (7, 'Магазин «у дома»'),
        (8, 'Гипермаркет'),
        (9, 'Cash&Carry'),
        (10, 'Прилавок/киоск'),
        (11, 'Частное предприятие'),
    )
    company_type = models.IntegerField(verbose_name='Тип компании:', choices=COMPANY_TYPES)
    user = models.ForeignKey(Users, verbose_name='Пользователь:', on_delete=models.CASCADE)

#Модель еды
class Food(models.Model):
    name = models.CharField(verbose_name='Название:', max_length=128)
    description = models.TextField(verbose_name='Описание:', blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена:')
    quantity = models.PositiveIntegerField(verbose_name='Кол-во:')
    image = models.ImageField(verbose_name='Фото:', upload_to='images')
    FOOD_TYPES = (
        (1, 'Мясо и мясопродукты'),
        (2, 'Рыба и морепродукты'),
        (3, 'Молоко и молокопродукты'),
        (4, 'Овощи и фрукты'),
        (5, 'Пекарня'),
        (6, 'Кондитерская'),
        (7, 'Консервы'),
        (8, 'Бакалея'),
        (9, 'Кулинария'),
        (10, 'Частная компания')
    )
    food_type = models.IntegerField(verbose_name='Тип продукта:', choices=FOOD_TYPES)
    company = models.ForeignKey(Company, verbose_name='Компания:', on_delete=models.CASCADE, related_name='company')

#сделать отзывы(текстовые)