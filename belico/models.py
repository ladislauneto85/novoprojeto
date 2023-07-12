from django.db import models

class Belico(models.Model):

    TIPO_CHOICES = [
        (1, 'PISTOLA'),
        (2, 'ARMA LONGA'),
    ]

    MODELO_CHOICES = [
        (1, 'PT 100'),
        (2, 'SMT'),
        (3, 'CT'),  
    ]

    numero_serie = models.CharField('NÚMERO DE SÉRIE', max_length=8)
    tipo = models.IntegerField(verbose_name='TIPO', choices=TIPO_CHOICES)
    modelo = models.IntegerField(verbose_name='MODELO', choices=MODELO_CHOICES)

    def __str__(self):
        return str(self.numero_serie)
    
    class Meta:
        verbose_name = 'Cadastro de Arma'
        verbose_name_plural = 'Cadastro de Armas'
