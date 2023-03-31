# Generated by Django 4.1.7 on 2023-03-31 03:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["username"],
                "permissions": (
                    (
                        "download_cancer_report",
                        "Puede descargar reportes del registro de cáncer",
                    ),
                ),
            },
        ),
    ]
