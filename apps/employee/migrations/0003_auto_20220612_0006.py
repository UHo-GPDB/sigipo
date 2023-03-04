# Generated by Django 3.2.13 on 2022-06-12 00:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0002_alter_doctor_last_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="doctor",
            options={
                "default_permissions": (),
                "ordering": ["personal_record_number"],
                "verbose_name": "Doctor",
                "verbose_name_plural": "Doctor",
            },
        ),
        migrations.AlterModelOptions(
            name="group",
            options={
                "default_permissions": (),
                "ordering": ["pk"],
                "verbose_name": "Grupo",
                "verbose_name_plural": "Grupo",
            },
        ),
    ]
