from django.forms import (
    CharField, TextInput,
    DateTimeField, DateTimeInput, 
    Textarea, Select, JSONField,
    ChoiceField,)

from apps.death_certificate.models import DeathCertificate, ScholarshipLevelChoices, CivilStateChoices, ResidenceTypeChoices, DeathPlaceChoices, PregnancyChoices, PregnancyResultChoices, ConfirmationCausesChoices, CertficationMadeByChoices, LastSurgeriesChoices, ViolentDeathCausesChoices
from apps.patient.forms import BasePatientForm


class DeathCertificateForm(BasePatientForm):
    """Model to handle DeathCertificate creation and edition."""

    deathCertificate_number = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Número de Certificación de Defunción",
            },
        ),
        label="Número de Certificación de Defunción",
    )
    
    direct_death_cause = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Causa de Muerte"}),
        label="Causa de Muerte",
    )

    indirect_death_cause = JSONField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Causa que ocasionó"}),
        label="Causa que ocasionó",
    )

    indirect_death_cause = JSONField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Causa que ocasionó"}),
        label="Causa que ocasionó",
    )

    indirect_death_cause = JSONField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Causa que ocasionó"}),
        label="Causa que ocasionó",
    )


    other_contibuting_diseases = JSONField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Otras enfermedades contribuyentes"}),
        label="Otras enfermedades contribuyentes",
    )
    ocupation = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Ocupación"}),
        label="Ocupación",
    )
    
    time_of_death = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de defunción",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha de defunción",
    )

    ScholarshipLevel = ChoiceField(
        choices=ScholarshipLevelChoices.choices,
        initial=ScholarshipLevelChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Nivel de Escolaridad",
    )

    CivilState = ChoiceField(
        choices=CivilStateChoices.choices,
        initial=CivilStateChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Estado Cívil",
    )

    ResidenceType = ChoiceField(
        choices=ResidenceTypeChoices.choices,
        initial=ResidenceTypeChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo de Residencia",
    )

    DeathPlace = ChoiceField(
        choices=DeathPlaceChoices.choices,
        initial=DeathPlaceChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Sitio de Defunción",
    )

    Pregnancy = ChoiceField(
        choices=PregnancyChoices.choices,
        initial=PregnancyChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Embarazo en los últimos 12 meses",
    )

    PregnancyResult = ChoiceField(
        choices=PregnancyResultChoices.choices,
        initial=PregnancyResultChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Resultado del embarazo",
    )

    date_of_pregnancy = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha del embarazo",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha del embarazo",
    )

    ConfirmationCauses = ChoiceField(
        choices=ConfirmationCausesChoices.choices,
        initial=ConfirmationCausesChoices.CLINIC,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Certificación realizada por médico de",
    )

    CertficationMadeBy = ChoiceField(
        choices=CertficationMadeByChoices.choices,
        initial=CertficationMadeByChoices.HGCORP,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Certificación realizada por médico de",
    )

    LastSurgeries = ChoiceField(
        choices=LastSurgeriesChoices.choices,
        initial=LastSurgeriesChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="CCirugías en las últimas 4 semanas",
    )

    ViolentDeathCauses = ChoiceField(
        choices=ViolentDeathCausesChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Causa aparente de muerte violenta",
    )
   
    date_of_injury = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de la lesión",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha de la lesión",
    )

    place_where_injury_occurred = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Lugar donde ocurrio la lesión"}),
        label="Lugar donde ocurrio la lesión",
    )

    event_description = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Descripcion de como ocurrio"}),
        label="Descripcion de como ocurrio",
    )

    Requesting_authority = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Autoridad que solicita"}),
        label="Autoridad que solicita",
    )

    Act_number = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Número de Acta"}),
        label="Número de Acta",
    )

    Surgery_reasons = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Causa de la Cirugía"}),
        label="Causa de la Cirugía",
    )

    class Meta:
        model = DeathCertificate
        fields = "__all__"
