# Generated by Django 3.2 on 2021-05-06 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_remove_cartitem_total_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_item',
            field=models.IntegerField(default=0),
        ),
    ]