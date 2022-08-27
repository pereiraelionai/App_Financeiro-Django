from django.db import models


class Cadastro(models.Model):
    data = models.DateField()
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    valor = models.FloatField()
