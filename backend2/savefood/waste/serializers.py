from rest_framework import serializers
from . import models
from shop.serializers import UserInfoTrashSerializers

class TrashSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Trash
        fields = '__all__'

class TrashInfoSerializers(serializers.ModelSerializer):
    user = UserInfoTrashSerializers()
    class Meta:
        model = models.Trash
        fields = '__all__'