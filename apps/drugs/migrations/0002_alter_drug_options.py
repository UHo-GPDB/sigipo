# Generated by Django 3.2.13 on 2022-05-12 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("drugs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="drug",
            options={
                "ordering": ["pk"],
                "verbose_name": "Fármaco",
                "verbose_name_plural": "Fármacos",
            },
        ),
    ]
