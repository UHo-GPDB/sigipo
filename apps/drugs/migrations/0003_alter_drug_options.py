# Generated by Django 3.2.13 on 2022-06-12 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("drugs", "0002_rename_type_drug_drug_type"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="drug",
            options={
                "default_permissions": (),
                "ordering": ["pk"],
                "verbose_name": "Fármaco",
                "verbose_name_plural": "Fármacos",
            },
        ),
    ]
