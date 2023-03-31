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
from apps.core.fields import RelatedModelWrapper
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
        model = Scheme
        fields = "__all__"


class ProtocolForm(ModelForm):
    """Model to handle Protocol creation and edition."""

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
                "first_name__trigram_similar",
                "last_name__trigram_similar",
                "identity_card__trigram_similar",
                "medical_record__trigram_similar",
            ],
            add_url="patient:oncologic_create",
            view_url="patient:oncologic_detail",
            add_permission="patient.add_oncologic",
            view_permission="patient.view_oncologic",
        ),
        label="Paciente",
    )
    scheme = ModelChoiceField(
        queryset=Scheme.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Esquema",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__trigram_similar",
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
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Médico que reporta",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "first_name__trigram_similar",
                "last_name__trigram_similar",
                "personal_record_number__trigram_similar",
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
        model = Protocol
        fields = "__all__"


class MedicationForm(ModelForm):
    """Model to handle Medication creation and edition."""

    protocol = ModelChoiceField(
        queryset=Protocol.objects.not_suspended(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Protocolo",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "patient__first_name__trigram_similar",
                "patient__last_name__trigram_similar",
                "patient__identity_card__trigram_similar",
                "patient__medical_record__trigram_similar",
            ],
        ),
        label="Protocolo",
    )
    drug = ModelChoiceField(
        queryset=Drug.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Fármaco",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__trigram_similar",
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
        model = Medication
        fields = "__all__"


class CycleForm(ModelForm):
    protocol = ModelChoiceField(
        queryset=Protocol.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Protocolo",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "patient__first_name__trigram_similar",
                "patient__last_name__trigram_similar",
                "patient__identity_card__trigram_similar",
                "patient__medical_record__trigram_similar",
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
        model = Cycle
        fields = "__all__"


class CycleMedicationForm(ModelForm):
    drug = ModelChoiceField(
        queryset=Drug.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Fármaco",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__trigram_similar",
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
        model = CycleMedication
        fields = ("drug", "dose", "unit")
