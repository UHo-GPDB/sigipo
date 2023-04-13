# Generated by Django 4.1.6 on 2023-04-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("death_certificate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="deathcertificate",
            name="indirect_death_cause_1",
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name="deathcertificate",
            name="indirect_death_cause_2",
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name="deathcertificate",
            name="indirect_death_cause_3",
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name="deathcertificate",
            name="other_contibuting_diseases",
            field=models.JSONField(default={}),
        ),
    ]
