# Generated by Django 3.2.16 on 2023-02-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('death_certificate', '0002_auto_20230207_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='deathcertificate',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
    ]