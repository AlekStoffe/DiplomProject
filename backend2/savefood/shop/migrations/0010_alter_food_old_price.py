# Generated by Django 3.2 on 2021-05-07 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210508_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='old_price',
            field=models.IntegerField(blank=True, verbose_name='Старая цена'),
        ),
    ]