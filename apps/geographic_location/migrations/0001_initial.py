# Generated by Django 3.2.13 on 2022-05-23 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Province",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Provincia",
                "verbose_name_plural": "Provincias",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Municipality",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Nombre")),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geographic_location.province",
                        verbose_name="Provincia",
                    ),
                ),
            ],
            options={
                "verbose_name": "Municipio",
                "verbose_name_plural": "Municipios",
                "ordering": ["pk"],
            },
        ),
    ]
