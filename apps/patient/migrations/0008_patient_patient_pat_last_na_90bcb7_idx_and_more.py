# Generated by Django 4.1.7 on 2023-03-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0007_alter_patient_options"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="patient",
            index=models.Index(
                fields=["last_name", "first_name"],
                name="patient_pat_last_na_90bcb7_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="patient",
            index=models.Index(
                fields=["first_name"], name="patient_pat_first_n_b4754d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="patient",
            index=models.Index(
                fields=["last_name"], name="patient_pat_last_na_f630ca_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="patient",
            index=models.Index(
                fields=["identity_card"], name="patient_pat_identit_403e47_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="patient",
            index=models.Index(
                fields=["medical_record"], name="patient_pat_medical_738b43_idx"
            ),
        ),
    ]