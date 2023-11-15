# Generated by Django 4.2.1 on 2023-11-14 18:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0020_neckbiopsydiagnostic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="neckbiopsydiagnostic",
            old_name="otros_margenes_reseccion_endoscopica",
            new_name="otros_margenes_EE",
        ),
        migrations.RenameField(
            model_name="neckbiopsydiagnostic",
            old_name="otros_margenes_reseccion_endoscopica_especificaciones",
            new_name="otros_margenes_EE_especificaciones",
        ),
        migrations.RenameField(
            model_name="neckbiopsydiagnostic",
            old_name="otros_margenes_sophagectomia_y_esophagogastrectomia",
            new_name="otros_margenes_RE",
        ),
        migrations.RenameField(
            model_name="neckbiopsydiagnostic",
            old_name="otros_margenes_sophagectomia_y_esophagogastrectomia_especificaciones",
            new_name="otros_margenes_RE_especificaciones",
        ),
    ]