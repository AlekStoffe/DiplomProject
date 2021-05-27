from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Trash(models.Model):
    name = models.CharField(verbose_name='Название отходов:', max_length=128)
    username = models.CharField(verbose_name='Имя:', max_length=128)
    description = models.TextField(verbose_name='Описание:', blank=True)
    period = models.TextField(verbose_name='Период:', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во:')
    telephone = models.CharField(verbose_name='Телефон:', max_length=11, blank=True)
    point = models.CharField(verbose_name='Адрес:', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фото:', upload_to='images', default='images/trash.jpg')
    user = models.ForeignKey(User, verbose_name='Пользователь:', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Trash, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class TrashGive(models.Model):
    name = models.CharField(verbose_name='Название отходов:', max_length=128)
    username = models.CharField(verbose_name='Имя:', max_length=128)
    description = models.TextField(verbose_name='Описание:', blank=True)
    period = models.TextField(verbose_name='Период:', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во:')
    telephone = models.CharField(verbose_name='Телефон:', max_length=11)
    date = models.DateTimeField(verbose_name='К какому дню')
    point = models.CharField(verbose_name='Адрес:', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фото:', upload_to='images', default='images/trash.jpg')
    user = models.ForeignKey(User, verbose_name='Пользователь:', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(TrashGive, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)