# Generated by Django 4.1.6 on 2023-04-10 17:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("geographic_location", "0003_location"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="municipality",
            options={
                "ordering": ["pk"],
                "verbose_name": "Municipio",
                "verbose_name_plural": "Municipios",
            },
        ),
        migrations.AlterModelOptions(
            name="province",
            options={
                "ordering": ["pk"],
                "verbose_name": "Provincia",
                "verbose_name_plural": "Provincias",
            },
        ),
    ]