# Generated by Django 4.2.1 on 2023-06-08 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patient", "0001_initial"),
        ("employee", "0001_initial"),
        (
            "classifiers",
            "0003_alter_morphology_options_alter_radioisotope_options_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Neoplasm",
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
                (
                    "date_of_diagnosis",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de diagnóstico"
                    ),
                ),
                (
                    "age_at_diagnosis",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Edad al momento de diagnóstico",
                    ),
                ),
                ("psa", models.FloatField(blank=True, null=True, verbose_name="PSA")),
                (
                    "laterality",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "No"), (2, "Derecho"), (3, "Izquierdo")],
                        null=True,
                        verbose_name="Lateralidad",
                    ),
                ),
                (
                    "diagnostic_confirmation",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Clínica"),
                            (2, "Investigación Clínica"),
                            (4, "Marcadores Tumorales"),
                            (5, "Citología"),
                            (6, "Histología de una metástasis"),
                            (7, "Histología del tumor primario"),
                            (9, "Desconocido"),
                        ],
                        null=True,
                        verbose_name="Confirmación del Diagnóstico",
                    ),
                ),
                (
                    "differentiation_grade",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "Diferenciado"),
                            (2, "Moderadamente diferenciado"),
                            (3, "Poco diferenciado"),
                            (4, "Indiferenciado"),
                            (5, "Células T"),
                            (6, "Células B"),
                            (7, "Células nulas"),
                            (8, "Células NK"),
                            (9, "No determinado"),
                        ],
                        null=True,
                        verbose_name="Grado de diferenciación",
                    ),
                ),
                (
                    "clinical_extension",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "In situ"),
                            (2, "Localizada"),
                            (3, "Extesión Directa"),
                            (4, "Linfática Regional"),
                            (5, "Extensión Directa y Linfática Regional"),
                            (6, "Metástasis remota"),
                            (7, "No aplicable"),
                            (8, "Desconocido"),
                        ],
                        null=True,
                        verbose_name="Extensión clínica",
                    ),
                ),
                (
                    "clinical_stage",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (0, "In Situ"),
                            (1, "I"),
                            (2, "Ia"),
                            (3, "Ib"),
                            (4, "Ic"),
                            (5, "II"),
                            (6, "IIa"),
                            (7, "IIb"),
                            (8, "IIc"),
                            (9, "III"),
                            (10, "IIIa"),
                            (11, "IIIb"),
                            (12, "IIIc"),
                            (13, "IV"),
                            (14, "IVa"),
                            (15, "IVb"),
                            (16, "IVc"),
                            (17, "Desconocido"),
                            (18, "No Aplicable"),
                        ],
                        null=True,
                        verbose_name="Etapa clínica",
                    ),
                ),
                (
                    "is_pregnant",
                    models.BooleanField(default=False, verbose_name="¿Embarazada?"),
                ),
                (
                    "trimester",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Trimestre"
                    ),
                ),
                (
                    "is_vih",
                    models.BooleanField(default=False, verbose_name="¿Es VIH+?"),
                ),
                (
                    "source_of_info",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Anatomía patológica"),
                            (2, "Hematología"),
                            (3, "Egreso hospitalario"),
                            (4, "Registro de fallecidos"),
                        ],
                        null=True,
                        verbose_name="Fuente de información",
                    ),
                ),
                (
                    "date_of_report",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha del reporte"
                    ),
                ),
                (
                    "tumor",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("TXTX", "Tx"),
                            ("T0", "T0"),
                            ("Tis", "Tis"),
                            ("T1", "T1"),
                            ("T2", "T2"),
                            ("T3", "T3"),
                            ("T4", "T4"),
                        ],
                        max_length=10,
                        null=True,
                        verbose_name="Tumor",
                    ),
                ),
                (
                    "nodule",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("NX", "NX"),
                            ("N0", "N0"),
                            ("N1", "N1"),
                            ("N2", "N2"),
                            ("N3", "N3"),
                        ],
                        max_length=10,
                        null=True,
                        verbose_name="Nódulo",
                    ),
                ),
                (
                    "metastasis",
                    models.CharField(
                        blank=True,
                        choices=[("MX", "MX"), ("M0", "M0"), ("M1", "M1")],
                        max_length=10,
                        null=True,
                        verbose_name="Metástasis",
                    ),
                ),
                (
                    "neoplasm_classification",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "Clínico"), (2, "Patológico")],
                        null=True,
                        verbose_name="Clínico o Patológico",
                    ),
                ),
                (
                    "tumor_classification",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Tumor primario"),
                            (2, "Metástasis sin tumor primario conocido"),
                        ],
                        null=True,
                        verbose_name="Clasificación",
                    ),
                ),
                (
                    "treatment_performed",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Cirugía"),
                            (2, "Quimioterapia"),
                            (3, "Radioterapia"),
                            (4, "Hormonoterapia"),
                            (0, "Ninguno"),
                        ],
                        null=True,
                        verbose_name="Tratamiento realizado",
                    ),
                ),
                (
                    "hematological_transformation",
                    models.BooleanField(
                        default=False, verbose_name="Transformación hematológica"
                    ),
                ),
                (
                    "date_of_first_symptoms",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de primeros síntomas"
                    ),
                ),
                (
                    "acute_lymphoid_leukemia",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "L1"), (2, "L2"), (3, "L3")],
                        null=True,
                        verbose_name="Leucemia linfoide aguda (FAB)",
                    ),
                ),
                (
                    "chronic_lymphoid_leukemia",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "0"), (2, "I"), (3, "II"), (4, "III"), (5, "IV")],
                        null=True,
                        verbose_name="Leucemia linfoide crónica (Rail)",
                    ),
                ),
                (
                    "acute_myeloid_leukemia",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "M0"),
                            (1, "M1"),
                            (2, "M2"),
                            (3, "M3"),
                            (4, "M4"),
                            (5, "M5"),
                            (6, "M6"),
                            (7, "M7"),
                        ],
                        null=True,
                        verbose_name="Leucemia mieloide aguda (FAB)",
                    ),
                ),
                (
                    "multiple_myeloma",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Ia"),
                            (2, "Ib"),
                            (3, "IIa"),
                            (4, "IIb"),
                            (5, "IIIa"),
                            (6, "IIIb"),
                        ],
                        null=True,
                        verbose_name="Mieloma múltiple (Durie-Salmon)",
                    ),
                ),
                (
                    "chronic_myeloid_leukemia",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Estable"),
                            (2, "Acelerada"),
                            (3, "Crisis blástica "),
                        ],
                        null=True,
                        verbose_name="Leucemia mieloide crónica",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.group",
                        verbose_name="Grupo que reporta",
                    ),
                ),
                (
                    "histologic_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classifiers.morphology",
                        verbose_name="Tipo histológico",
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
                (
                    "primary_site",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classifiers.topography",
                        verbose_name="Sitio primario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Neoplasia",
                "verbose_name_plural": "Neoplasias",
                "ordering": ["pk"],
            },
        ),
    ]
