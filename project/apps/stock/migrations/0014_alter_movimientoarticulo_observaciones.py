# Generated by Django 3.2.4 on 2024-02-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_auto_20240108_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientoarticulo',
            name='observaciones',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Observaciones'),
        ),
    ]
