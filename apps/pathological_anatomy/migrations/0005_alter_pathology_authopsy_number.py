# Generated by Django 3.2.16 on 2023-03-03 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathological_anatomy", "0004_alter_pathology_authopsy_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pathology",
            name="authopsy_number",
            field=models.CharField(
                default=django.db.models.deletion.SET_NULL,
                max_length=50,
                primary_key=True,
                serialize=False,
                verbose_name="Número de Autopsia",
            ),
        ),
    ]
