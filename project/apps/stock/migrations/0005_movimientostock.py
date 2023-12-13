# Generated by Django 3.2.4 on 2023-12-13 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('stock', '0004_remove_movimientoarticulo_articulo_foraneo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id_origen', models.PositiveIntegerField()),
                ('object_id_destino', models.PositiveIntegerField()),
                ('cantidad', models.IntegerField()),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('salida', 'Salida')], max_length=10)),
                ('usuario', models.CharField(default='', max_length=50, verbose_name='Usuario')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Movimiento de Stock',
                'verbose_name_plural': 'Movimientos de Stock',
            },
        ),
    ]
