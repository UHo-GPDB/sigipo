# Generated by Django 3.2.13 on 2022-06-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drugs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drug",
            name="out_of_stock",
            field=models.BooleanField(verbose_name="¿En falta?"),
        ),
    ]