from rest_framework import serializers
from . import models

class TrashSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Trash
        fields = '__all__'

class TrashGiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TrashGive
        fields = '__all__'

class TrashInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Trash
        fields = '__all__'

class TrashGiveInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TrashGive
        fields = '__all__'