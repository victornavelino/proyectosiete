# Generated by Django 3.2.4 on 2022-11-11 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0024_precio_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='observaciones',
            field=models.CharField(max_length=10, null=True, verbose_name='Observaciones'),
        ),
    ]
