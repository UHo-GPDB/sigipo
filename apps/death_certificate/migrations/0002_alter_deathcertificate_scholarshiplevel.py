# Generated by Django 4.1.6 on 2023-03-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("death_certificate", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deathcertificate",
            name="ScholarshipLevel",
            field=models.IntegerField(
                choices=[
                    (0, "Ninguno"),
                    (1, "Primaria"),
                    (2, "Secundaria Básica"),
                    (3, "Obrero Calificado"),
                    (4, "Pre-Universitario"),
                    (5, "Técnico Medio"),
                    (6, "Universitario"),
                    (7, "Ignorado(a)"),
                ],
                default=7,
                verbose_name="Nivel de Escolaridad",
            ),
        ),
    ]
