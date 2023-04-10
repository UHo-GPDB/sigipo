from django.forms import (
    CharField,
    ChoiceField,
    DateTimeField,
    DateTimeInput,
    JSONField,
    ModelChoiceField,
    Select,
    Textarea,
)
from django_select2.forms import ModelSelect2Widget

from apps.core.fields import RelatedModelWrapper
from apps.core.forms import ModelForm
from apps.core.widget import CauseOfDeathField
from apps.death_certificate.models import (
    CertficationMadeByChoices,
    CivilStateChoices,
    ConfirmationCausesChoices,
    DeathCertificate,
    DeathPlaceChoices,
    LastSurgeriesChoices,
    PregnancyChoices,
    PregnancyResultChoices,
    ResidenceTypeChoices,
    ScholarshipLevelChoices,
    ViolentDeathCausesChoices,
)
from apps.geographic_location.models import Location
from apps.patient.models import Patient


class DeathCertificateForm(ModelForm):
    """Model to handle DeathCertificate creation and edition."""

    patient = ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Paciente",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "first_name__icontains",
                "last_name__icontains",
                "identity_card__icontains",
                "medical_record__icontains",
            ],
        ),
        label="Paciente",
    )

    direct_death_cause = CharField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Causa de Muerte"}
        ),
        label="Causa de Muerte",
    )

    indirect_death_cause_1 = CauseOfDeathField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Causa que ocasionó I"}
        ),
        label="Causa que ocasionó",
    )

    indirect_death_cause_2 = CauseOfDeathField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Causa que ocasionó II"}
        ),
        label="Causa que ocasionó",
    )

    indirect_death_cause_3 = CauseOfDeathField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Causa que ocasionó III"}
        ),
        label="Causa que ocasionó",
    )

    other_contibuting_diseases = JSONField(
        widget=Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Otras enfermedades contribuyentes",
            }
        ),
        label="Otras enfermedades contribuyentes",
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

    scholarship_level = ChoiceField(
        choices=ScholarshipLevelChoices.choices,
        initial=ScholarshipLevelChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Nivel de Escolaridad",
    )

    civil_state = ChoiceField(
        choices=CivilStateChoices.choices,
        initial=CivilStateChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Estado Cívil",
    )

    residence_type = ChoiceField(
        choices=ResidenceTypeChoices.choices,
        initial=ResidenceTypeChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo de Residencia",
    )

    death_place = ChoiceField(
        choices=DeathPlaceChoices.choices,
        initial=DeathPlaceChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Sitio de Defunción",
    )

    pregnancy = ChoiceField(
        choices=PregnancyChoices.choices,
        initial=PregnancyChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Embarazo en los últimos 12 meses",
    )

    pregnancy_result = ChoiceField(
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

    confirmation_causes = ChoiceField(
        choices=ConfirmationCausesChoices.choices,
        initial=ConfirmationCausesChoices.CLINIC,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Certificación de Causas",
    )

    certfication_made_by = ChoiceField(
        choices=CertficationMadeByChoices.choices,
        initial=CertficationMadeByChoices.HGCORP,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Certificación realizada por médico de",
    )

    last_surgeries = ChoiceField(
        choices=LastSurgeriesChoices.choices,
        initial=LastSurgeriesChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="CCirugías en las últimas 4 semanas",
    )

    violent_death_causes = ChoiceField(
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
        widget=Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Lugar donde ocurrio la lesión",
            }
        ),
        label="Lugar donde ocurrio la lesión",
    )

    event_description = CharField(
        widget=Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Descripcion de como ocurrio",
            }
        ),
        label="Descripcion de como ocurrio",
    )

    requesting_authority = CharField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Autoridad que solicita"}
        ),
        label="Autoridad que solicita",
    )

    act_number = CharField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Número de Acta"}
        ),
        label="Número de Acta",
    )

    surgery_reasons = CharField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Causa de la Cirugía"}
        ),
        label="Causa de la Cirugía",
    )

    death_location = ModelChoiceField(
        queryset=Location.objects.all(),
        label="Localidad de defunción",
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Localidad de defunción",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
                "province__name__icontains",
                "municipality__name__icontains",
            ],
        ),
    )

    class Meta:
        model = DeathCertificate
        fields = "__all__"
