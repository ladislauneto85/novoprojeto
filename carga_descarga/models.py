from django.db import models
from accounts.models import CadastroPolicial
from belico.models import Belico

class CargaDescarga(models.Model):     

    belico = models.ForeignKey(Belico, on_delete=models.CASCADE, verbose_name='BÉLICO')
    quantidade = models.PositiveIntegerField(blank=False)
    sub_quantidade = models.PositiveIntegerField(blank=False)
    policial = models.ForeignKey(CadastroPolicial, on_delete=models.CASCADE, verbose_name='POLICIAL')
    
    
