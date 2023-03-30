from django.db.models import (
    SET_NULL,
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    IntegerChoices,
    IntegerField,
    JSONField,
    Model,
    OneToOneField,
    TextField,
)

from apps.geographic_location.models import Location
from apps.patient.models import Patient


class ScholarshipLevelChoices(IntegerChoices):
    """Defines the Death Scholarship Level."""

    NONE = 0, "Ninguno"
    PRIMARY = 1, "Primaria"
    SECUNDARY = 2, "Secundaria Básica"
    QWORKER = 3, "Obrero Calificado"
    PREUNIVERSITARY = 4, "Pre-Universitario"
    ITECHNICIAN = 5, "Técnico Medio"
    UNIVERSITY = 6, "Universitario"
    UNDEFINED = 7, "Ignorado(a)"


class CivilStateChoices(IntegerChoices):
    """Defines the Death Civil State."""

    MARRIED = 1, "Casado(a)"
    UNITED = 2, "Unido"
    DIVORCE = 3, "Divorciado"
    SEPARATE = 4, "Seaprado"
    WIDOW = 5, "Viudo"
    SINGLE = 6, "Soltero"
    UNDEFINED = 7, "Ignorado(a)"


class ResidenceTypeChoices(IntegerChoices):
    """Defines the Death Residence Type."""

    PERMANENT = 1, "Permanente"
    TEMPORAL = 2, "Temporal"
    UNDEFINED = 3, "Ignorado(a)"


class DeathPlaceChoices(IntegerChoices):
    """Defines the Death Death Place."""

    HGCORP = 1, "Cuerpo de Guardia Hospitalario"
    HADMINSSION = 2, "Ingreso Hospitalario"
    POLYCLINIC = 3, "Policlínico"
    OTHERMEDICALCENTER = 4, "Otro Centro Hospitalario"
    RESIDENCE = 5, "Domicilio"
    OTHERPLACE = 6, "Otro Lugar"
    UNDEFINED = 7, "Ignorado(a)"


class PregnancyChoices(IntegerChoices):
    """Defines the Death Pregnancy in the last 12 month."""

    YES = 1, "Sí"
    NO = 2, "No"
    UNDEFINED = 3, "Ignorado(a)"


class PregnancyResultChoices(IntegerChoices):
    """Defines the Death Pregnancy Result."""

    ABORTION = 1, "Aborto"
    CESAREANDELIVERY = 2, "Parto por Cesarea"
    PELVICHILDBIRTH = 3, "Parto Pelviano"
    DIEDPREGNANT = 4, "Murio estando embarazada"
    UNDEFINED = 5, "Ignorado(a)"


class ConfirmationCausesChoices(IntegerChoices):
    """Defines the Death Confirmation Causes."""

    CLINIC = 1, "Clinica"
    INVESTIGATION = 2, "Investigación"
    OPERATION = 3, "Operación"
    BIOPSY = 4, "Biopsia"
    NECROPSY = 5, "Necropsia"
    RECOGNITION = 6, "Reconocimiento"


class CertficationMadeByChoices(IntegerChoices):
    """Defines the Death Certfication made by Doctor."""

    HGCORP = 1, "Guardia"
    ASISTENCY = 2, "Asistencia"
    FAMILY = 3, "Familia"
    LEGIST = 4, "Legista"
    OTHER = 5, "Otro"


class LastSurgeriesChoices(IntegerChoices):
    """Defines the Death Last Surgeries in the last 4 months."""

    YES = 1, "Sí"
    NO = 2, "No"
    UNDEFINED = 3, "Ignorado(a)"


class ViolentDeathCausesChoices(IntegerChoices):
    """Defines the Death Violent Death Causes."""

    ACCIDENT = 1, "Accidente"
    SUICIDE = 2, "Suicidio"
    HOMICIDE = 3, "Homicidio"
    OTHER = 4, "Otro"
    CINVESTIGATION = 5, "Por Investigar"


class DeathCertificate(Model):
    """Model representation of a death_certificate."""

    patient = OneToOneField(Patient, null=True, blank=False, on_delete=SET_NULL)

    deathCertificate_number = CharField(
        verbose_name="Número de Certificación de Defunción",
        max_length=50,
        primary_key=True,
        default=None,
    )

    direct_death_cause = TextField(verbose_name="Causa de Muerte")

    indirect_death_cause = JSONField(verbose_name="Causa que ocasionó")
    indirect_death_cause = JSONField(verbose_name="Causa que ocasionó")
    indirect_death_cause = JSONField(verbose_name="Causa que ocasionó")

    other_contibuting_diseases = JSONField(verbose_name="Otras enfermedades contribuyentes")


    time_of_death = DateTimeField(
        verbose_name="Fecha de defunción",
        blank=True,
        null=True,
        auto_now_add=True,
    )
    first_name = CharField(verbose_name="Nombre", max_length=128)
    last_name = CharField(verbose_name="Apellidos", max_length=255)
    ocupation = CharField(verbose_name="Ocupación", max_length=128)

    ScholarshipLevel = IntegerField(
        verbose_name="Nivel de Escolaridad",
        choices=ScholarshipLevelChoices.choices,
        default=ScholarshipLevelChoices.UNDEFINED,
    )

    CivilState = IntegerField(
        verbose_name="Estado Cívil",
        choices=CivilStateChoices.choices,
        default=CivilStateChoices.UNDEFINED,
    )

    ResidenceType = IntegerField(
        verbose_name="Tipo de Residencia",
        choices=ResidenceTypeChoices.choices,
        blank=True,
        null=True,
    )

    DeathPlace = IntegerField(
        verbose_name="Sitio de Defunción",
        choices=DeathPlaceChoices.choices,
        default=DeathPlaceChoices.UNDEFINED,
    )

    Pregnancy = IntegerField(
        verbose_name="Embarazo en los últimos 12 meses",
        choices=PregnancyChoices.choices,
        default=PregnancyChoices.UNDEFINED,
    )

    PregnancyResult = IntegerField(
        verbose_name="Resultado del embarazo",
        choices=PregnancyResultChoices.choices,
        blank=True,
        null=True,
    )
    date_of_pregnancy = DateField(
        verbose_name="Fecha del embarazo",
        blank=True,
        null=True,
    )

    ConfirmationCauses = IntegerField(
        verbose_name="Confirmación de las causas",
        choices=ConfirmationCausesChoices.choices,
        default=ConfirmationCausesChoices.CLINIC,
    )

    CertficationMadeBy = IntegerField(
        verbose_name="Certificación realizada por médico de",
        choices=CertficationMadeByChoices.choices,
        default=CertficationMadeByChoices.HGCORP,
    )

    LastSurgeries = IntegerField(
        verbose_name="Cirugías en las últimas 4 semanas",
        choices=LastSurgeriesChoices.choices,
        default=LastSurgeriesChoices.UNDEFINED,
    )

    Surgery_reasons = TextField(verbose_name="Causa de la Cirugía")

    ViolentDeathCauses = IntegerField(
        verbose_name="Causa aparente de muerte violenta",
        choices=ViolentDeathCausesChoices.choices,
        blank=True,
        null=True,
    )

    date_of_injury = DateField(
        verbose_name="Fecha de la lesión",
        blank=True,
        null=True,
    )

    place_where_injury_occurred = TextField(
        verbose_name="Lugar donde ocurrio la lesión"
    )
    event_description = TextField(verbose_name="Descripcion de como ocurrio")
    Requesting_authority = TextField(verbose_name="Autoridad que solicita")
    Act_number = TextField(verbose_name="Número de Acta")

    death_location = ForeignKey(
        Location,
        verbose_name="Localidad de defunción",
        related_name="residence_location_death",
        null=True,
        on_delete=SET_NULL,
    )

    class Meta:
        verbose_name = "Certificado de Defunción"
        verbose_name_plural = "Certificados de Defunción"
        ordering = ["pk"]
        default_permissions = ()

    def __str__(self):
        """String representation of death_certificate."""
        return f"{self.name}"
