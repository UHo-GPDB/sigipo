# Generated by Django 4.2.1 on 2023-05-30 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patient", "0009_view_name_change"),
        ("employee", "0004_alter_doctor_options_alter_group_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="BiopsyRequest",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "biopsy_id",
                    models.CharField(
                        max_length=100, null=True, verbose_name="No Biopsia"
                    ),
                ),
                (
                    "hospital",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Hospital Lenin"),
                            (2, "Hospital Clinico"),
                            (3, "hospital Pediatrico"),
                            (4, "Hosptal Militar"),
                        ],
                        null=True,
                        verbose_name="Hospital",
                    ),
                ),
                (
                    "sample_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de la muestra"
                    ),
                ),
                (
                    "health_area",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Area de Salud",
                    ),
                ),
                (
                    "especiality",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Especialidad",
                    ),
                ),
                (
                    "age",
                    models.IntegerField(blank=True, null=True, verbose_name="Edad"),
                ),
                (
                    "sex",
                    models.IntegerField(
                        choices=[(0, "No definido"), (1, "Masculino"), (2, "Femenino")],
                        default=0,
                        verbose_name="Sexo",
                    ),
                ),
                (
                    "race",
                    models.IntegerField(
                        choices=[
                            (0, "No Definido"),
                            (1, "Blanca"),
                            (2, "Negra"),
                            (3, "Mestizo"),
                            (4, "Amarillo"),
                        ],
                        default=0,
                        verbose_name="Raza",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Direeción Particular",
                    ),
                ),
                (
                    "biopsy_type",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Biopsia de mama"),
                            (2, "Biopsia de Cuello"),
                            (3, "Siopsia Digestivo"),
                            (4, "Biopsia de Linfoma"),
                            (5, "Biopsia de Ginecologia"),
                            (6, "Biopsia de Cabeza"),
                        ],
                        null=True,
                        verbose_name="Tipo de Biopsia",
                    ),
                ),
                (
                    "sample_biopsy",
                    models.CharField(max_length=250, verbose_name="Tipo de Muestra"),
                ),
                (
                    "clinic_data",
                    models.CharField(max_length=255, verbose_name="Datos Clinicos"),
                ),
                (
                    "clinic_diagnostic",
                    models.CharField(
                        max_length=255, verbose_name="Diagnostico Clinico"
                    ),
                ),
                (
                    "medic_that_report",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.doctor",
                        verbose_name="Médico que reporta",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                        verbose_name="Paciente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Solicitud de Biopsia",
                "verbose_name_plural": "Solicitudes de Biopsias",
                "ordering": ["pk"],
            },
        ),
    ]