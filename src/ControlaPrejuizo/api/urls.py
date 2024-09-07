from django.urls import path
from . import views

urlpatterns = [
    path('listar_compras/', views.listar_compras, name='listar_compras'),
    path('adicionar_compra/', views.adicionar_compra, name='adicionar_compra'),
    path('visualizar_compra/<int:id_compra>/', views.visualizar_compra, name='visualizar_compra'),
    path('editar_compra/<int:id_compra>/', views.editar_compra, name='editar_compra'),
    path('apagar_compra/<int:id_compra>/', views.apagar_compra, name='apagar_compra'),
]
