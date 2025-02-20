from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cliente, Pedidos, ItensPedido
from .serializers import ClienteSerializer, PedidosSerializer, ItensPedidoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidosViewSet(ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


class ItensPedidoViewSet(ModelViewSet):
    queryset = ItensPedido.objects.all()
    serializer_class = ItensPedidoSerializer 




# Create your views here.
