# Generated by Django 3.2 on 2021-05-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0002_alter_trash_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Фото:'),
        ),
    ]
