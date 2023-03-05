# Generated by Django 3.2.13 on 2022-07-22 09:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "default_permissions": (),
                "ordering": ["username"],
                "permissions": (
                    (
                        "patient_manage",
                        "Puede Crear/Modificar/Eliminar datos de pacientes no oncologicos",
                    ),
                    (
                        "cancer_registry_view",
                        "Puede visualizar datos del registro de cáncer",
                    ),
                    (
                        "cancer_registry_manage",
                        "Puede Crear/Modificar/Eliminar datos del registro de cáncer",
                    ),
                    (
                        "download_cancer_report",
                        "Puede descargar reportes del registro de cáncer",
                    ),
                    (
                        "nuclear_medicine_view",
                        "Puede visualizar datos de medicina nuclear.",
                    ),
                    (
                        "nuclear_medicine_manage",
                        "Puede Crear/Modificar/Eliminar datos de medicina nuclear",
                    ),
                    ("drug_view", "Puede visualizar fármacos."),
                    ("drug_manage", "Puede Crear/Modificar/Eliminar datos de fármacos"),
                    ("employee_view", "Puede visualizar fármacos."),
                    (
                        "employee_manage",
                        "Puede Crear/Modificar/Eliminar datos de grupos de trabajo/médicos",
                    ),
                ),
            },
        ),
    ]
