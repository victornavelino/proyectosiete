# Generated by Django 3.2.4 on 2022-05-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0010_auto_20220509_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
