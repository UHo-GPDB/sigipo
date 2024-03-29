# Generated by Django 4.1.7 on 2023-05-04 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geographic_location", "0002_auto_20220612_0006"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="municipality",
            options={
                "ordering": ["pk"],
                "verbose_name": "Municipio",
                "verbose_name_plural": "Municipios",
            },
        ),
        migrations.AlterModelOptions(
            name="province",
            options={
                "ordering": ["pk"],
                "verbose_name": "Provincia",
                "verbose_name_plural": "Provincias",
            },
        ),
        migrations.CreateModel(
            name="Location",
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
                    "municipality",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geographic_location.municipality",
                        verbose_name="Municipio",
                    ),
                ),
            ],
            options={
                "verbose_name": "Loacalidad",
                "verbose_name_plural": "Loacalidades",
                "ordering": ["pk"],
            },
        ),
    ]
