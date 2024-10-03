from django.urls import path
from .views import * 

urlpatterns = [
    # GET
    path('', listar_compras, name='listar_compras'),
    path('<int:id_compra>/', visualizar_compra, name='visualizar_compra'),
    path('filtrar/', listar_compras, name='listar_compras_sem_filtro'),
    path('filtrar/ano/<int:ano>/', filtrar_compras_ano, name='filtrar_compras_ano'),
    path('filtrar/mes/<int:mes>-<int:ano>/', filtrar_compras_mes, name='filtrar_compras_mes'),
    path('filtrar/periodo/<int:dia_inicio>-<int:mes_inicio>-<int:ano_inicio>/<int:dia_limite>-<int:mes_limite>-<int:ano_limite>/', filtrar_compras_periodo, name='filtrar_compras_periodo'),
    path('filtrar/metodo-pagamento/<str:metodo_pagamento>/', filtrar_metodo_pagamento, name='filtrar_metodo-pagamento'),
    path('filtrar/categoria/<str:categoria>/', filtrar_categoria, name='filtrar_categoria'),
    path('filtrar/utilidade/<str:utilidade>/', filtrar_utilidade, name='filtrar_utilidade'),

    # POST
    path('adicionar/', adicionar_compra, name='adicionar_compra'),

    # DELETE
    path('apagar/<int:id_compra>/', apagar_compra, name='apagar_compra'),

    # PUT
    path('editar/<int:id_compra>/', editar_compra, name='editar_compra'),

    # PATCH
    path('editar/<int:id_compra>/<str:campo>/', editar_campo, name='editar_campo'),
]
