# Generated by Django 3.2 on 2021-05-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_food_old_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='old_price',
            field=models.CharField(blank=True, max_length=15, verbose_name='Старая цена'),
        ),
    ]