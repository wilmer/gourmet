# Generated by Django 2.1.4 on 2020-02-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_entrada_platodefondo_refresco'),
    ]

    operations = [
        migrations.CreateModel(
            name='registroestado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_registroestado', models.CharField(max_length=12)),
            ],
        ),
    ]