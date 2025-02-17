from django.contrib import admin
from .models import Cliente, Pedidos, ItensPedido

admin.site.register(Cliente)
admin.site.register(Pedidos)
admin.site.register(ItensPedido)


# Register your models here.
