import random
import string

from django.db import models
from django.contrib.auth.models import User

def gera_senha(size=8, chars=string.ascii_uppercase + string.digits):
    # gera um código de 8 dígitos (padrão) em UPPERCASE + números
    return ''.join(random.choice(chars) for _ in range(size))

def password_is_valid(user, senha) -> bool:
    # recebe um USER, pode ser do request como request.user
    # e devolve True ou False para a assinatura do policial
    return user.CadastroPolicial.senha == senha

class CadastroPolicial(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField('MATRÍCULA', max_length=8)
    nome = models.CharField('NOME COMPLETO', max_length=50)
    senha = models.CharField(max_length=8)

    def save(self, *args, **kwargs):
        # gera a senha apenas na criação do objeto
        if not self.pk:
            self.senha = gera_senha()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.matricula)
    
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'


