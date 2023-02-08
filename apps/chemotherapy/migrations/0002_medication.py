# Generated by Django 3.2.13 on 2022-06-22 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drugs", "0002_alter_drug_out_of_stock"),
        ("chemotherapy", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medication",
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
                ("days", models.IntegerField(verbose_name="Días")),
                (
                    "route",
                    models.IntegerField(
                        choices=[
                            (0, "Intramuscular"),
                            (1, "Intravenosa"),
                            (2, "Subcutaneo"),
                            (3, "Intradérmica"),
                            (4, "Oral"),
                        ],
                        verbose_name="Via de administración",
                    ),
                ),
                ("prescribed_dose", models.FloatField(verbose_name="Dosis prescrita")),
                (
                    "unit",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "g"), (1, "mg"), (2, "ml")],
                        null=True,
                        verbose_name="Unidad",
                    ),
                ),
                ("suspended", models.BooleanField(verbose_name="Suspendido")),
                (
                    "cause",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Causa"
                    ),
                ),
                (
                    "drug",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drugs.drug",
                        verbose_name="Medicamento",
                    ),
                ),
                (
                    "protocol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chemotherapy.protocol",
                        verbose_name="Protocolo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Medicación",
                "verbose_name_plural": "Medicaciones",
                "ordering": ["pk"],
                "default_permissions": (),
            },
        ),
    ]
