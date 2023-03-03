# Generated by Django 3.2.16 on 2023-02-24 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radiations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='externalbeamreg',
            name='fractionation',
        ),
        migrations.RemoveField(
            model_name='externalbeamtreat',
            name='external_beam_config',
        ),
        migrations.RemoveField(
            model_name='externalbeamtreat',
            name='target_precision',
        ),
        migrations.RemoveField(
            model_name='internalradiationreg',
            name='fractionation',
        ),
        migrations.AddField(
            model_name='externalbeamtreat',
            name='biopsy',
            field=models.TextField(blank=True, null=True, verbose_name='Biopsia'),
        ),
        migrations.AddField(
            model_name='internalradiationtreatment',
            name='biopsy',
            field=models.TextField(blank=True, null=True, verbose_name='Biopsia'),
        ),
        migrations.AlterField(
            model_name='externalbeamreg',
            name='treat_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='radiations.externalbeamtreat'),
        ),
        migrations.AlterField(
            model_name='externalbeamtreat',
            name='treat_number',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Numero de Tratamiento'),
        ),
        migrations.AlterField(
            model_name='internalradiationreg',
            name='treat_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='radiations.internalradiationtreatment'),
        ),
        migrations.AlterField(
            model_name='internalradiationtreatment',
            name='treat_number',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Numero de Tratamiento'),
        ),
    ]