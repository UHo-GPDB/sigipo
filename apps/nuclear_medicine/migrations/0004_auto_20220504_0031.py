# Generated by Django 3.2.13 on 2022-05-04 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nuclear_medicine", "0003_hormonalresult_oncologicresult"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hormonalresult",
            name="hormonal_study",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="nuclear_medicine.patienthormonalstudy",
            ),
        ),
        migrations.AlterField(
            model_name="oncologicresult",
            name="oncologic_study",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="nuclear_medicine.patientoncologicstudy",
            ),
        ),
    ]