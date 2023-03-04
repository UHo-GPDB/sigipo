# Generated by Django 3.2.13 on 2022-06-04 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Grupo",
                "verbose_name_plural": "Grupo",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "first_name",
                    models.CharField(
                        max_length=255,
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Apellidos"),
                ),
                (
                    "personal_record_number",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Número de registro",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.group",
                        verbose_name="Grupo de trabajo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Doctor",
                "verbose_name_plural": "Doctor",
                "ordering": ["personal_record_number"],
            },
        ),
    ]
