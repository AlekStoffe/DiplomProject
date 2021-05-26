from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from . import models
import django_filters.rest_framework

# Create your views here.
class TrashCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TrashSerializers

class TrashListView(generics.ListAPIView):
    queryset = models.Trash.objects.all()
    serializer_class = TrashSerializers

class TrashIdView(generics.ListAPIView):
    queryset = models.Trash.objects.all()
    serializer_class = TrashInfoSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ['id',]