# Generated by Django 3.2.13 on 2022-06-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cancer_registry", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="neoplasm",
            name="metastasis",
            field=models.CharField(
                blank=True,
                choices=[("MX", "MX"), ("M0", "M0"), ("M1", "M1")],
                max_length=10,
                verbose_name="Metástasis",
            ),
        ),
        migrations.AddField(
            model_name="neoplasm",
            name="neoplasm_classification",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Clínico"), (2, "Patológico")],
                null=True,
                verbose_name="Clínico o Patológico",
            ),
        ),
        migrations.AddField(
            model_name="neoplasm",
            name="nodule",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NX", "NX"),
                    ("N0", "N0"),
                    ("N1", "N1"),
                    ("N2", "N2"),
                    ("N3", "N3"),
                ],
                max_length=10,
                verbose_name="Nódulo",
            ),
        ),
        migrations.AddField(
            model_name="neoplasm",
            name="tumor",
            field=models.CharField(
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
                verbose_name="Tumor",
            ),
        ),
        migrations.AddField(
            model_name="neoplasm",
            name="tumor_classification",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Tumor primario"),
                    (2, "Metástasis sin tumor primario conocido"),
                ],
                null=True,
                verbose_name="Clasificación",
            ),
        ),
        migrations.DeleteModel(
            name="TNM",
        ),
    ]