# Generated by Django 4.2.1 on 2023-11-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0038_alter_stomacbiopsydiagnostic_tipo_muestra"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stomacbiopsydiagnostic",
            name="grado_histologico",
            field=models.IntegerField(
                choices=[
                    (1, "G1: El bien diferenciado"),
                    (2, "G2: Moderadamente diferenciado"),
                    (3, "G3: Pobremente diferenciado, no diferenciado"),
                    (4, "otro (especifique)"),
                    (5, "GX: No puede ser evaluado"),
                    (6, "no se aplica"),
                ],
                verbose_name="El Grado del Histológico",
            ),
        ),
    ]