from django.db import models
import datetime

class Compra(models.Model):
    escolha_metodo_pagamento = [
        ('Dinheiro', 'Dinheiro'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
        ('Pix', 'Pix'),
        ('Boleto', 'Boleto'),
        ('Outro', 'Outro'),
    ]

    escolha_categoria = [
        ('Tecnologia', 'Tecnologia'),
        ('Alimentação', 'Alimentação'),
        ('Cuidado pessoal', 'Cuidado Pessoal'),
        ('Transporte', 'Transporte'),
        ('Vestuário', 'Vestuário'),
        ('Saúde', 'Saúde'),
        ('Lazer', 'Lazer'),
        ('Moradia', 'Moradia'),
        ('Educação', 'Educação'),
        ('Contratação de serviço', 'Contratação de serviço'),
        ('Outro', 'Outro'),
    ]

    produto = models.CharField(max_length=100, blank=False)
    valor = models.FloatField(blank=False)
    data_compra = models.DateField(default=datetime.date.today)
    categoria = models.CharField(choices=escolha_categoria, max_length=30, blank=True, default='-')
    metodo_pagamento = models.CharField(choices=escolha_metodo_pagamento, max_length=20, blank=False)
    descricao = models.CharField(max_length=150, blank=True, default='-')
