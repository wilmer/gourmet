# Generated by Django 2.1.4 on 2020-02-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='descripcion_entrada',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='platodefondo',
            name='descripcion_platodefondo',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='refresco',
            name='descripcion_refresco',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='registroestado',
            name='descripcion_registroestado',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
