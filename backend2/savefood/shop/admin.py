from django.contrib import admin
from . import  models

admin.site.register(models.Company)
admin.site.register(models.Food)
admin.site.register(models.Profile)

