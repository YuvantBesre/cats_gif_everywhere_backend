from django.contrib import admin
from .models import CatData

# Register your models here.

@admin.register(CatData)
class CatData(admin.ModelAdmin):
    pass