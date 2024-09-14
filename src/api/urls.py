from django.urls import path
from .views import * 

urlpatterns = [
    path('listar-compras/', listar_compras, name='listar_compras'),
    path('adicionar-compra/', adicionar_compra, name='adicionar_compra'),
    path('visualizar-compra/<int:id_compra>/', visualizar_compra, name='visualizar_compra'),
    path('editar-compra/<int:id_compra>/', editar_compra, name='editar_compra'),
    path('editar-compra/<int:id_compra>/<str:campo>/', editar_campo, name='editar_campo'),
    path('apagar-compra/<int:id_compra>/', apagar_compra, name='apagar_compra'),
    path('filtrar-compras/ano/<int:ano>/', filtrar_compras_ano, name='filtrar_compras_ano'),
    path('filtrar-compras/mes/<int:mes>-<int:ano>/', filtrar_compras_mes, name='filtrar_compras_mes'),
    path('filtrar-compras/metodo-pagamento/<str:metodo_pagamento>/', filtrar_metodo_pagamento, name='filtrar_metodo-pagamento'),
    path('filtrar-compras/categoria/<str:categoria>/', filtrar_categoria, name='filtrar_categoria'),
    path('filtrar-compras/utilidade/<str:utilidade>/', filtrar_utilidade, name='filtrar_utilidade'),
]
