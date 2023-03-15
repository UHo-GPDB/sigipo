# Generated by Django 3.2.16 on 2023-03-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("radiations", "0004_auto_20230227_1221"),
    ]

    operations = [
        migrations.AlterField(
            model_name="externalbeamtreat",
            name="treat_number",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="Número de Tratamiento"
            ),
        ),
        migrations.AlterField(
            model_name="internalradiationtreatment",
            name="treat_number",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="Numero de Tratamiento"
            ),
        ),
    ]
