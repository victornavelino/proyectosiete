# Generated by Django 3.2.4 on 2022-08-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0030_auto_20220715_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
