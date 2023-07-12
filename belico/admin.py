from django.contrib import admin
from .models import Belico

@admin.register(Belico)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('numero_serie', 'tipo', 'modelo')
