# Generated by Django 2.1.4 on 2020-02-23 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_pedidoatendido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='descripcion_pedido',
            field=models.CharField(max_length=250, null=True),
        ),
    ]