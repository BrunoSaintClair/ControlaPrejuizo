from django.db import models
import datetime

class Compra(models.Model):
    produto = models.CharField(max_length=100)
    valor = models.FloatField()
    data_compra = models.DateField(default=datetime.date.today)
    metodo_pagamento = models.CharField(max_length=100)