from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    ChoiceField,
    DateField,
    DateInput,
    FloatField,
    IntegerField,
    ModelChoiceField,
    NumberInput,
    Select,
    TextInput,
)
from django_select2.forms import ModelSelect2Widget

from apps.cancer_registry.models import NeoplasmClinicalStageChoices
from apps.chemotherapy.models import (
    Cycle,
    CycleMedication,
    Medication,
    Protocol,
    RoomChoices,
    RouteChoices,
    Scheme,
)
from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm
from apps.drugs.models import Drug, UnitChoicesChoices
from apps.employee.models import Doctor
from apps.patient.models import Patient


class SchemeForm(ModelForm):
    """Model to handle Scheme creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        """Scheme Meta class."""

        model = Scheme
        fields = "__all__"


class ProtocolForm(ModelForm):
    """Model to handle Protocol creation and edition."""

    patient = ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=ModelSelect2Widget(
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
    scheme = ModelChoiceField(
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
    room = EmptyChoiceField(
        empty_label="----------",
        choices=RoomChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Lugar",
    )
    height = IntegerField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Talla (cm)",
            },
        ),
        label="Talla (cm)",
    )
    weight = FloatField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Peso (Kg)",
            },
        ),
        label="Peso (Kg)",
    )
    cycles = IntegerField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ciclos",
            },
        ),
        label="Ciclos",
    )
    stage = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmClinicalStageChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Etapa",
    )
    doctor = ModelChoiceField(
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
                "first_name__icontains",
                "last_name__icontains",
                "personal_record_number__icontains",
            ],
        ),
        label="Médico que reporta",
    )
    suspended = BooleanField(
        label="Suspendido",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )

    class Meta:
        """Protocol Meta class."""

        model = Protocol
        fields = "__all__"


class MedicationForm(ModelForm):
    """Model to handle Medication creation and edition."""

    protocol = ModelChoiceField(
        queryset=Protocol.objects.not_suspended(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Protocolo",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "patient__first_name__icontains",
                "patient__last_name__icontains",
                "patient__identity_card__icontains",
                "patient__medical_record__icontains",
            ],
        ),
        label="Protocolo",
    )
    drug = ModelChoiceField(
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
    days = IntegerField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Días",
            },
        ),
        label="Días",
    )
    route = ChoiceField(
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Via de administración",
        choices=RouteChoices.choices,
    )
    prescribed_dose = FloatField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Dosis prescrita",
            },
        ),
        label="Dosis prescrita",
    )
    unit = EmptyChoiceField(
        choices=UnitChoicesChoices.choices,
        empty_label="----------",
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Unidad"},
        ),
        label="Unidad",
        required=False,
    )
    suspended = BooleanField(
        label="Suspendido",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )
    cause = CharField(
        label="Causa",
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Causa"}),
        required=False,
    )

    class Meta:
        """Medication Meta class."""

        model = Medication
        fields = "__all__"


class CycleForm(ModelForm):
    """Model to handle Cycle creation and edition."""

    protocol = ModelChoiceField(
        queryset=Protocol.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Protocolo",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "patient__first_name__icontains",
                "patient__last_name__icontains",
                "patient__identity_card__icontains",
                "patient__medical_record__icontains",
            ],
        ),
        label="Protocolo",
    )
    next_date = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de próximo ciclo",
                "type": "date",
            },
            format="%Y-%m-%d",
        ),
        label="Fecha de próximo ciclo",
        required=False,
    )

    class Meta:
        """Cycle Meta class."""

        model = Cycle
        fields = "__all__"


class CycleMedicationForm(ModelForm):
    """Model to handle CycleMedication creation and edition."""

    drug = ModelChoiceField(
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
    dose = FloatField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Dosis",
            },
        ),
        label="Dosis",
    )
    unit = EmptyChoiceField(
        choices=UnitChoicesChoices.choices,
        empty_label="----------",
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Unidad"},
        ),
        label="Unidad",
        required=False,
    )

    class Meta:
        """CycleMedication Meta class."""

        model = CycleMedication
        fields = ("drug", "dose", "unit")
