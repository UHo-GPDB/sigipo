from django.forms import TextInput, NumberInput
from django_filters import CharFilter, FilterSet, NumberFilter, ModelChoiceFilter
from django_select2.forms import ModelSelect2Widget
from apps.employee.models import Doctor

from apps.radiotherapy.models import (
    Physicist,
    Dosimetrist,
    Technic,
    TACRequest,
    Disease,
    Treatment,
    GeneralDatasheet,

)

from config.settings.base import FIELD_SEARCH_LOOKUP


class PhysicistFilter(FilterSet):
    ''' Filter Criteria for the Physicist Model '''
    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Physicist
        fields = [
            "name",
        ]

class DosimetristFilter(FilterSet):
    ''' Filter Criteria for the Dosimetrist Model '''
    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Dosimetrist
        fields = [
            "name",
        ]

class TACRequestFilter(FilterSet):
    id_code = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "ID contiene"}
        ),
        label="Código ID",
    )

    patient__identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet",
    )

    patient__first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombres",
    )

    patient__last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos",
    )
    
    patient__medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica",
    )

    bb_position = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Posición del BB contiene",
            }
        ),
        label="Posición del BB",
    )

    location = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Localización contiene",
            }
        ),
        label="Localización",
    )

    upper_limit = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Límite Superior contiene",
            }
        ),
        label="Límite Superior",
    )
    
    lower_limit = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Límite Inferior contiene",
            }
        ),
        label="Límite Inferior",
    )

    distance_betwen_cuts = NumberFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
        label="Distancia entre cortes (mm)",
    )

    medic_that_requests = ModelChoiceFilter(
        queryset=Doctor.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Doctor que Solicita",
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
        label="Doctor que Solicita",
    )

    physicist = ModelChoiceFilter(
        queryset=Physicist.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Físico",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Físico",
    )

    dosimetrist = ModelChoiceFilter(
        queryset=Dosimetrist.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Dosimetrista",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Dosimetrista",
    )

    class Meta:
        model = TACRequest
        fields = [
            "id_code",
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "bb_position",
            "location",
            "upper_limit",
            "lower_limit",
            "distance_betwen_cuts",
            "medic_that_requests",
            "physicist",
            "dosimetrist",
        ]

class TechnicFilter(FilterSet):
    ''' Filter Criteria for the Technic Model '''
    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Technic
        fields = [
            "name",
        ]

class DiseaseFilter(FilterSet):
    ''' Filter Criteria for the Disease Model '''
    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Disease
        fields = [
            "name",
        ]

class TreatmentFilter(FilterSet):
    ''' Filter Criteria for the Treatment Model '''
    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Treatment
        fields = [
            "name",
        ]

class GeneralDatasheetFilter(FilterSet):
    id_code = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "ID contiene"}
        ),
        label="Código ID",
    )

    patient__identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet",
    )

    patient__first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombres",
    )

    patient__last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos",
    )
    
    patient__medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica",
    )

    class Meta:
        model = GeneralDatasheet
        fields = [
            "id_code",
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
        ]