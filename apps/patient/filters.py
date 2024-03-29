from django.forms import NullBooleanSelect, Select, TextInput
from django_filters import (
    BooleanFilter,
    CharFilter,
    ChoiceFilter,
    FilterSet,
    ModelChoiceFilter,
    RangeFilter,
)
from django_filters.widgets import RangeWidget
from django_select2.forms import ModelSelect2Widget

from apps.geographic_location.models import Municipality, Province
from apps.patient.models import Patient, PatientRace
from config.settings.base import FIELD_SEARCH_LOOKUP


class CustomRangeWidget(RangeWidget):
    """Widget to set different placeholder to each field."""

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.widgets[0].attrs.update(
            {"class": "form-control", "placeholder": "Edad de diagnóstico mínima"}
        )
        self.widgets[1].attrs.update(
            {"class": "form-control", "placeholder": "Edad de diagnóstico máxima"}
        )


class PatientFilter(FilterSet):
    """Filters to search for patients."""

    identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    race = ChoiceFilter(
        choices=PatientRace.choices,
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Raza"}
        ),
    )
    residence_municipality = ModelChoiceFilter(
        queryset=Municipality.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Municipio de residencia",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
                f"province__name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Municipio de residencia",
    )
    born_municipality = ModelChoiceFilter(
        queryset=Municipality.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Municipio natal",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
                f"province__name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Municipio natal",
    )
    residence_municipality__province = ModelChoiceFilter(
        queryset=Province.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Provincia de residencia",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Provincia de residencia",
    )
    born_municipality__province = ModelChoiceFilter(
        queryset=Province.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Provincia natal",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Provincia natal",
    )
    age_at_diagnosis = RangeFilter(
        label="Edad de diagnóstico",
        widget=CustomRangeWidget,
    )

    class Meta:
        model = Patient
        fields = [
            "identity_card",
            "first_name",
            "last_name",
            "medical_record",
            "race",
            "residence_municipality",
            "born_municipality",
            "age_at_diagnosis",
        ]


class NuclearMedicinePatientFilter(PatientFilter):
    is_oncologic = BooleanFilter(
        widget=NullBooleanSelect(
            attrs={
                "class": "form-control form-select",
                "placeholder": "¿Es oncológico?",
            }
        ),
        label="¿Es oncológico?",
    )

    class Meta:
        model = Patient
        fields = [
            "identity_card",
            "first_name",
            "last_name",
            "medical_record",
            "race",
            "residence_municipality",
            "born_municipality",
            "age_at_diagnosis",
            "is_oncologic",
        ]
