from rest_framework.serializers import ModelSerializer
from alunos.models import Cliente, ItensPedido, Pedidos

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ItensPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'


class PedidosSerializer(ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


