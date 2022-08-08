from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    ativa = models.BooleanField(default=True)
    data_nascimento = models.DateField(null=True)
