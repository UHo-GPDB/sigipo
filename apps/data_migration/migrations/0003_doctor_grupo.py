# Generated by Django 3.2.13 on 2022-06-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_migration", "0002_localizacion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("grupo", models.CharField(max_length=255)),
                (
                    "id",
                    models.IntegerField(
                        db_column="id_grupo", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "tn_grupo",
                "abstract": False,
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Grupo",
            fields=[
                ("grupo", models.CharField(max_length=255)),
                (
                    "id",
                    models.IntegerField(
                        db_column="id_grupo", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "tn_grupo",
                "abstract": False,
                "managed": False,
            },
        ),
    ]