from django.contrib import admin
from .models import CargaDescarga

@admin.register(CargaDescarga)
class CargaDescargaAdmin(admin.ModelAdmin):
    list_display = ('belico', 'quantidade', 'sub_quantidade', 'policial')
