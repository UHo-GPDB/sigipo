from django.forms import Select, TextInput
from django_filters import CharFilter, ChoiceFilter, FilterSet, ModelChoiceFilter
from django_select2.forms import ModelSelect2Widget

from apps.cancer_registry.models import NeoplasmClinicalStageChoices
from apps.chemotherapy.models import (
    Medication,
    Protocol,
    RoomChoices,
    RouteChoices,
    Scheme,
)
from apps.drugs.models import Drug
from apps.employee.models import Doctor


class SchemeFilter(FilterSet):
    """Scheme Filter"""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        """Scheme Filter Meta class"""

        model = Scheme
        fields = [
            "name",
        ]


class ProtocolFilter(FilterSet):
    """Protocol Filter"""

    patient__identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    patient__first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    patient__last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    patient__medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    scheme = ModelChoiceFilter(
        queryset=Scheme.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Esquema",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
            ],
        ),
        label="Esquema",
    )
    room = ChoiceFilter(
        choices=RoomChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Lugar",
    )
    stage = ChoiceFilter(
        choices=NeoplasmClinicalStageChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Etapa",
    )
    doctor = ModelChoiceFilter(
        queryset=Doctor.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Doctor que reporta",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "first_name__icontains",
                "last_name__icontains",
                "personal_record_number__icontains",
            ],
        ),
        label="Doctor que reporta",
    )
    suspended = ChoiceFilter(
        choices=((True, "Suspendido"), (False, "Activo")),
        label="Suspendido",
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Suspendido"}
        ),
    )

    class Meta:
        """Protocol Filter Meta class"""

        model = Protocol
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "scheme",
            "room",
            "stage",
            "doctor",
            "suspended",
        ]


class MedicationFilter(FilterSet):
    """Medication Filter"""

    protocol__patient__identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    protocol__patient__first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    protocol__patient__last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    protocol__patient__medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    route = ChoiceFilter(
        choices=RouteChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Via de administración",
    )
    drug = ModelChoiceFilter(
        queryset=Drug.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Fármaco",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
            ],
        ),
        label="Fármaco",
    )
    suspended = ChoiceFilter(
        choices=((True, "Suspendido"), (False, "Activo")),
        label="Suspendido",
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Suspendido"}
        ),
    )

    class Meta:
        """Medication Filter Meta class"""

        model = Medication
        fields = [
            "protocol__patient__identity_card",
            "protocol__patient__first_name",
            "protocol__patient__last_name",
            "protocol__patient__medical_record",
            "drug",
            "route",
            "suspended",
        ]


class CycleFilter(FilterSet):
    """Cycle Filter"""

    protocol__patient__identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    protocol__patient__first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    protocol__patient__last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    protocol__patient__medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    protocol__scheme = ModelChoiceFilter(
        queryset=Scheme.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Esquema",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
            ],
        ),
        label="Esquema",
    )

    class Meta:
        """Cycle Filter Meta class"""

        model = Medication
        fields = [
            "protocol__patient__identity_card",
            "protocol__patient__first_name",
            "protocol__patient__last_name",
            "protocol__patient__medical_record",
            "protocol__scheme",
        ]
