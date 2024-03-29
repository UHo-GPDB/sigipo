from django.forms import TextInput
from django_filters import CharFilter, FilterSet, ModelChoiceFilter
from django_select2.forms import ModelSelect2Widget

from apps.cancer_registry.models import Neoplasm
from apps.classifiers.models import Morphology, Topography
from apps.employee.models import Doctor, Group
from config.settings.base import FIELD_SEARCH_LOOKUP


class NeoplasmFilter(FilterSet):
    """Filters to search for patients."""

    patient__identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    patient__first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    patient__last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    patient__medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    primary_site = ModelChoiceFilter(
        queryset=Topography.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Sitio primario",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Sitio primario",
    )
    histologic_type = ModelChoiceFilter(
        queryset=Morphology.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Tipo histológico",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Tipo histológico",
    )
    group = ModelChoiceFilter(
        queryset=Group.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Grupo que reporta",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        required=False,
        label="Grupo que reporta",
    )
    medic_that_report = ModelChoiceFilter(
        queryset=Doctor.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Médico que reporta",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"first_name__{FIELD_SEARCH_LOOKUP}",
                f"last_name__{FIELD_SEARCH_LOOKUP}",
                f"personal_record_number__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Médico que reporta",
    )

    class Meta:
        model = Neoplasm
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
        ]
