# Generated by Django 3.2 on 2021-04-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210426_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='lat',
            field=models.FloatField(blank=True, verbose_name='Широта:'),
        ),
        migrations.AlterField(
            model_name='company',
            name='lon',
            field=models.FloatField(blank=True, verbose_name='Долгота:'),
        ),
    ]