from django.contrib import admin
from .models import CadastroPolicial


@admin.register(CadastroPolicial)
class PolicialAdmin(admin.ModelAdmin):
   
    list_display = ('matricula', 'nome', 'senha')
    
