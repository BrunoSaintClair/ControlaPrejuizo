from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Compra
from .serializers import CompraSerializer

@api_view(['GET'])
def listar_compras(request):
    compras = Compra.objects.all()
    serializer = CompraSerializer(compras, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def adicionar_compra(request):
    serializer = CompraSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def visualizar_compra(request, id_compra):
    try:
        compra = Compra.objects.get(pk=id_compra)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CompraSerializer(compra)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def editar_compra(request, id_compra):
    try:
        compra = Compra.objects.get(pk=id_compra)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    compra_editada = CompraSerializer(compra, data=request.data)
    if compra_editada.is_valid():
        compra_editada.save()
        return Response(compra_editada.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def apagar_compra(request, id_compra):
    try:
        compra_a_apagar = Compra.objects.get(pk=id_compra)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    compra_a_apagar.delete()
    return Response(status=status.HTTP_202_ACCEPTED)