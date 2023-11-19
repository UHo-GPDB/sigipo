# Generated by Django 3.2.16 on 2023-11-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0006_alter_head_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="head",
            name="localizacion_tumor",
            field=models.CharField(
                max_length=100,
                verbose_name="El sitio (o localización) del tumor (seleccione todo lo que aplique):",
            ),
        ),
        migrations.AlterField(
            model_name="head",
            name="niveles_ganglionares",
            field=models.CharField(
                max_length=100,
                verbose_name="Especifique Niveles Ganglionares (seleccione todo lo que aplique)",
            ),
        ),
    ]
