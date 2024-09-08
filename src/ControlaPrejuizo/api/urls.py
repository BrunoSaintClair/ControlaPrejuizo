from django.urls import path
from . import views

urlpatterns = [
    path('listar_compras/', views.listar_compras, name='listar_compras'),
    path('adicionar_compra/', views.adicionar_compra, name='adicionar_compra'),
    path('visualizar_compra/<int:id_compra>/', views.visualizar_compra, name='visualizar_compra'),
    path('editar_compra/<int:id_compra>/', views.editar_compra, name='editar_compra'),
    path('apagar_compra/<int:id_compra>/', views.apagar_compra, name='apagar_compra'),
    path('filtrar_compras/ano/<int:ano>/', views.filtrar_compras_ano, name='filtrar_compras_ano'),
    path('filtrar_compras/mes/<int:mes>-<int:ano>/', views.filtrar_compras_mes, name='filtrar_compras_mes'),
    path('filtrar_compras/metodo_pagamento/<str:metodo_pagamento>/', views.filtrar_metodo_pagamento, name='filtrar_metodo_pagamento'),
    path('filtrar_compras/categoria/<str:categoria>/', views.filtrar_categoria, name='filtrar_categoria'),
    path('filtrar_compras/utilidade/<str:utilidade>/', views.filtrar_utilidade, name='filtrar_utilidade'),
]
