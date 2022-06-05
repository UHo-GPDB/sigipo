# Generated by Django 3.2.13 on 2022-06-05 00:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0001_initial"),
        ("cancer_registry", "0002_auto_20220604_1823"),
    ]

    operations = [
        migrations.AlterField(
            model_name="neoplasm",
            name="medic_that_report",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employee.doctor",
                verbose_name="Médico que reporta",
            ),
        ),
    ]