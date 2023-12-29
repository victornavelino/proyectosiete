# Generated by Django 3.2.4 on 2023-12-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_auto_20231221_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimientoarticulo',
            old_name='lugar_object_id',
            new_name='destino_object_id',
        ),
        migrations.RenameField(
            model_name='movimientoarticulo',
            old_name='lugar_type',
            new_name='origen_type',
        ),
        migrations.RemoveField(
            model_name='movimientoarticulo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='movimientoarticulo',
            name='origen_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
