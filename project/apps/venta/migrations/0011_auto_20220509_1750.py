# Generated by Django 3.1.3 on 2022-05-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0010_alter_ventaarticulo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventaarticulo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
