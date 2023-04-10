# Generated by Django 4.1.6 on 2023-03-29 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geographic_location", "0002_auto_20220612_0006"),
    ]

    operations = [
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
                "verbose_name": "Loacalidad",
                "verbose_name_plural": "Loacalidades",
                "ordering": ["pk"],
                "default_permissions": (),
            },
        ),
    ]
