# Generated by Django 5.1.6 on 2025-02-17 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alunos.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alunos.pedidos')),
            ],
        ),
    ]
