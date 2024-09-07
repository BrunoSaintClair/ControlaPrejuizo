from django.db import models

class Compra(models.Model):
    produto = models.CharField(max_length=100)
    valor = models.FloatField()
    data_compra = models.DateField(auto_now_add=True)
    metodo_pagamento = models.CharField(max_length=100)