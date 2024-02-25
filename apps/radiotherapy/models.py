from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    ManyToManyField,
    Model,
    PositiveIntegerField,
    TextField,
)

from apps.employee.models import Doctor
from apps.patient.models import Patient

# Create your models here.

# Evaluate the posibility of moving Physicist to employee.models


class Physicist(Model):
    """
    Model representation of a Physicist (Only Name field for now)
    """

    name = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Nombre",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Físico"
        verbose_name_plural = "Físicos"
        ordering = ["pk"]


class Dosimetrist(Model):
    """
    Model representation of a Dosimetrist (Only Name field for now)
    """

    name = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Nombre",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Dosimetrista"
        verbose_name_plural = "Dosimetristas"
        ordering = ["pk"]


class Technic(Model):
    """
    Model representation of a Technic (Only Name field for now)
    """

    name = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Nombre",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"
        ordering = ["pk"]


class TACRequest(Model):
    """
    Model representation of a TAC request for planning
    """

    id_code = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="ID",
    )

    patient = ForeignKey(
        Patient,
        on_delete=CASCADE,
        verbose_name="Paciente",
    )

    date_of_request = DateField(
        verbose_name="Fecha de solicitud",
        blank=True,
        null=True,
    )

    bb_position = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Posición del BB",
    )

    location = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Localización",
    )

    upper_limit = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Límite Superior",
    )

    lower_limit = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Límite Inferior",
    )

    distance_betwen_cuts = PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Distancia entre Cortes (mm)",
    )

    medic_that_requests = ForeignKey(
        Doctor,
        verbose_name="Doctor",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )

    physicist = ForeignKey(
        Physicist,
        on_delete=CASCADE,
        verbose_name="Físico",
    )

    dosimetrist = ForeignKey(
        Dosimetrist,
        on_delete=CASCADE,
        verbose_name="Dosimetrista",
    )

    def __str__(self) -> str:
        return f"{self.id_code} - {self.patient}"

    class Meta:
        verbose_name = "Solicitud de TAC"
        verbose_name_plural = "Solicitudes de TAC"
        ordering = ["pk"]


class Disease(Model):
    """
    Model representation of a Disease
    """

    name = CharField(max_length=255, verbose_name="Nombre")

    description = TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Enfermedad"
        verbose_name_plural = "Enfermedades"
        ordering = ["pk"]


class Treatment(Model):
    """
    Model representation of a Treatment
    """

    name = CharField(max_length=255, verbose_name="Nombre")

    description = TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"
        ordering = ["pk"]


class GeneralDatasheet(Model):
    """
    Model representation of a Radiotherapy General Datasheet
    """

    id_code = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="ID",
    )

    patient = ForeignKey(
        Patient,
        on_delete=CASCADE,
        verbose_name="Paciente",
    )

    serv_proc = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Serv. Proc.",
    )

    amb = CharField(max_length=255, blank=True, null=True, verbose_name="Amb.")

    hosp = CharField(max_length=255, blank=True, null=True, verbose_name="Hosp.")

    no_locaclizacion = CharField(
        max_length=255, blank=True, null=True, verbose_name="No. Localización"
    )

    description = TextField(
        blank=True, null=True, verbose_name="Localización y Descripción"
    )

    anatopathologic_diagnose = TextField(
        blank=True, null=True, verbose_name="Diagnóstico Anatomopatológico"
    )

    related_diseases = ManyToManyField(Disease, verbose_name="Enfermedades Asociadas")

    prev_treatments = ManyToManyField(Treatment, verbose_name="Tratamientos Previos")

    t = CharField(max_length=255, blank=True, null=True, verbose_name="T")

    n = CharField(max_length=255, blank=True, null=True, verbose_name="N")

    m = CharField(max_length=255, blank=True, null=True, verbose_name="M")

    stage = CharField(max_length=255, blank=True, null=True, verbose_name="Etapa")

    date = DateField(
        verbose_name="Fecha",
        blank=True,
        null=True,
    )

    radiotherapist = ForeignKey(
        Doctor,
        verbose_name="Radioterapeuta",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )

    physicist = ForeignKey(
        Physicist,
        on_delete=CASCADE,
        verbose_name="Físico",
    )

    dosimetrist = ForeignKey(
        Dosimetrist,
        on_delete=CASCADE,
        verbose_name="Dosimetrista",
    )

    Technic = ForeignKey(
        Technic,
        on_delete=CASCADE,
        verbose_name="Técnico",
    )

    central_cons_date = DateField(
        verbose_name="Fecha de consulta Central",
        blank=True,
        null=True,
    )

    new_cases_cons_date = DateField(
        verbose_name="Fecha de consulta Casos Nuevos",
        blank=True,
        null=True,
    )

    first_stage_simulation_date = DateField(
        verbose_name="Fecha de Simulación 1ra Fase",
        blank=True,
        null=True,
    )

    second_stage_simulation_date = DateField(
        verbose_name="Fecha de Simulación 2da Fase",
        blank=True,
        null=True,
    )

    tac_date = DateField(
        verbose_name="Fecha de TAC",
        blank=True,
        null=True,
    )

    paint_date = DateField(
        verbose_name="Fecha de Pintado",
        blank=True,
        null=True,
    )

    planing_date = DateField(
        verbose_name="Fecha de Planificado",
        blank=True,
        null=True,
    )

    first_stage_treatment_start_date = DateField(
        verbose_name="Fecha inicio tratamiento 1ra Fase",
        blank=True,
        null=True,
    )

    second_stage_treatment_start_date = DateField(
        verbose_name="Fecha inicio tratamiento 2da Fase",
        blank=True,
        null=True,
    )

    registered_by = CharField(
        max_length=255, blank=True, null=True, verbose_name="Registrado por"
    )

    def __str__(self) -> str:
        return f"{self.id_code} - {self.patient}"

    class Meta:
        verbose_name = "Hoja de Datos Generales"
        verbose_name_plural = "Hojas de Datos Generales"
        ordering = ["pk"]
