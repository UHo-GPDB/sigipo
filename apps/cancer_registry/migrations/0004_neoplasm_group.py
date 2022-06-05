# Generated by Django 3.2.13 on 2022-06-05 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0001_initial"),
        ("cancer_registry", "0003_alter_neoplasm_medic_that_report"),
    ]

    operations = [
        migrations.AddField(
            model_name="neoplasm",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employee.group",
                verbose_name="Grupo que reporta",
            ),
        ),
    ]
