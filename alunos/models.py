from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nome}"
    
class Pedidos(models.Model):
    data_pedido = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
class ItensPedido(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - {self.quantidade}x"

# Create your models here.
