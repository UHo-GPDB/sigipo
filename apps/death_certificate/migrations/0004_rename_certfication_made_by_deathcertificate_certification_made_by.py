# Generated by Django 4.1.6 on 2023-04-13 01:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "death_certificate",
            "0003_alter_deathcertificate_indirect_death_cause_1_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="deathcertificate",
            old_name="certfication_made_by",
            new_name="certification_made_by",
        ),
    ]
