# Generated by Django 3.2.13 on 2022-05-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Morphology",
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
                    "name",
                    models.CharField(max_length=255, verbose_name="Nombre"),
                ),
            ],
            options={
                "verbose_name": "Morfología",
                "verbose_name_plural": "Morfologías",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="RadioIsotope",
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
                ("name", models.CharField(max_length=500)),
            ],
            options={
                "verbose_name": "Radio isótopo",
                "verbose_name_plural": "Radio isótopo",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Study",
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
                ("name", models.CharField(max_length=500)),
            ],
            options={
                "verbose_name": "Estudio",
                "verbose_name_plural": "Estudios",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Topography",
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
                    "name",
                    models.CharField(max_length=255, verbose_name="Nombre"),
                ),
            ],
            options={
                "verbose_name": "Topografía",
                "verbose_name_plural": "Topografías",
                "ordering": ["pk"],
            },
        ),
    ]
