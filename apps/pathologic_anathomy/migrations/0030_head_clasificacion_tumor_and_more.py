# Generated by Django 4.2.1 on 2023-11-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0029_remove_neckbiopsydiagnostic_clasificacion_tumor"),
    ]

    operations = [
        migrations.AddField(
            model_name="head",
            name="clasificacion_tumor",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "PT"), (2, "N"), (3, "M")],
                default=None,
                null=True,
                verbose_name="Clasificación Tumor",
            ),
        ),
        migrations.AddField(
            model_name="neckbiopsydiagnostic",
            name="clasificacion_tumor",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "PT"), (2, "N"), (3, "M")],
                default=None,
                null=True,
                verbose_name="Clasificación Tumor",
            ),
        ),
    ]
