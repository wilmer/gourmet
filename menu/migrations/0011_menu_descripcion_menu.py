# Generated by Django 2.1.4 on 2020-02-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20200222_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='descripcion_menu',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
