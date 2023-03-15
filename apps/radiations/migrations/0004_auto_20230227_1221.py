# Generated by Django 3.2.16 on 2023-02-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("radiations", "0003_auto_20230224_2128"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="externalbeamtreat",
            options={
                "default_permissions": (),
                "ordering": ["created_at"],
                "verbose_name": "Tratamiento Radiación Haz Externo",
                "verbose_name_plural": "Tratamientos Radiación Haz Externo",
            },
        ),
        migrations.AlterField(
            model_name="externalbeamtreat",
            name="radiation_time",
            field=models.TimeField(
                blank=True, null=True, verbose_name="Tiempo de Radiación"
            ),
        ),
        migrations.AlterField(
            model_name="externalbeamtreat",
            name="treat_number",
            field=models.AutoField(
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Número de Tratamiento",
            ),
        ),
    ]
