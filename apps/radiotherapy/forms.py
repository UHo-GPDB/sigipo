from django.forms import (
    CharField,
    ModelMultipleChoiceField,
    SelectMultiple,
    Textarea,
    TextInput,
    DateInput,
    NumberInput,
    IntegerField,
)
from apps.employee.models import Doctor
from apps.patient.models import Patient

from apps.radiotherapy.models import (
    Physicist,
    Dosimetrist,
    Technic,
    TACRequest,
    Disease,
    Treatment,
    GeneralDatasheet,
)
from apps.core.fields import RelatedModelWrapper
from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm, ModelChoiceField, DateField
from config.settings.base import FIELD_SEARCH_LOOKUP


class PhysicistForm(ModelForm):
    """Model to handle Physicist creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Physicist
        fields = "__all__"


class DosimetristForm(ModelForm):
    """Model to handle Dosimetrist creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Dosimetrist
        fields = "__all__"


class TACRequestForm(ModelForm):
    """Model to handle TAC Request creation and edition."""

    id_code = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "ID"}),
        label = "ID"
    )

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
                f"first_name__{FIELD_SEARCH_LOOKUP}",
                f"last_name__{FIELD_SEARCH_LOOKUP}",
                f"identity_card__{FIELD_SEARCH_LOOKUP}",
                f"medical_record__{FIELD_SEARCH_LOOKUP}",
            ],
            add_url="patient:oncologic_create",
            view_url="patient:oncologic_detail",
            add_permission="patient.add_oncologic",
            view_permission="patient.view_oncologic",
        ),
        label="Paciente",
    )

    date_of_request = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de Solicitud",
    )

    bb_position = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Posición del BB"}),
        label = "Posición del BB"
    )

    location = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Localización"}),
        label = "Localización"
    )

    upper_limit = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Límite superior"}),
        label = "Límite superior"
    )
    
    lower_limit = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Límite inferior"}),
        label = "Límite inferior"
    )

    distance_betwen_cuts = IntegerField(
        widget = NumberInput(attrs={"class": "form-control", "min":0}),
        label = "Distancia entre los cortes"
    )

    medic_that_requests = ModelChoiceField(
        queryset = Doctor.objects.all(),
        widget = RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Doctor",
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
        label="Doctor",
    )
    
    physicist = ModelChoiceField(
        queryset = Physicist.objects.all(),
        widget = RelatedModelWrapper(
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
    
    dosimetrist = ModelChoiceField(
        queryset = Dosimetrist.objects.all(),
        widget = RelatedModelWrapper(
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
        fields = "__all__"


class TechnicForm(ModelForm):
    """Model to handle Technic creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Technic
        fields = "__all__"


class DiseaseForm(ModelForm):
    """Model to handle Disease creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    description = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Descripción"}),
        label="Descripción",
    )

    class Meta:
        model = Disease
        fields = "__all__"


class TreatmentForm(ModelForm):
    """Model to handle Treatment creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    description = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Descripción"}),
        label="Descripción",
    )

    class Meta:
        model = Treatment
        fields = "__all__"


class GeneralDatasheetForm(ModelForm):
    """Model to handle General Datasheet creation and edition."""

    id_code = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "ID"}),
        label = "ID"
    )

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
                f"first_name__{FIELD_SEARCH_LOOKUP}",
                f"last_name__{FIELD_SEARCH_LOOKUP}",
                f"identity_card__{FIELD_SEARCH_LOOKUP}",
                f"medical_record__{FIELD_SEARCH_LOOKUP}",
            ],
            add_url="patient:oncologic_create",
            view_url="patient:oncologic_detail",
            add_permission="patient.add_oncologic",
            view_permission="patient.view_oncologic",
        ),
        label="Paciente",
    )

    serv_proc = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Serv. Proc."}),
        label = "Serv. Proc."
    )

    amb = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Amb."}),
        label = "Amb."
    )

    hosp = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Hosp."}),
        label = "Hosp."
    )

    no_locaclizacion = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "No. Localización"}),
        label = "No. Localización"
    )

    description = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Localización y Descripción"}),
        label="Localización y Descripción",
    )

    anatopathologic_diagnose = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Diagnóstico Anatomopatológico"}),
        label="Diagnóstico Anatomopatológico",
    )

    related_diseases = ModelMultipleChoiceField(
        queryset=Disease.objects.all(),
        widget=SelectMultiple(attrs={"class": "form-control"}),
        label="Enfermedades Asociadas",
    )

    
    prev_treatments = ModelMultipleChoiceField(
        queryset=Treatment.objects.all(),
        widget=SelectMultiple(attrs={"class": "form-control"}),
        label="Tratamientos Previos",
    )

    
    t = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "T"}),
        label = "T"
    )

    n = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "N"}),
        label = "N"
    )

    m = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "M"}),
        label = "M"
    )

    stage = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Etapa"}),
        label = "Etapa"
    )

    date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha",
    )

    radiotherapist = ModelChoiceField(
        queryset = Doctor.objects.all(),
        widget = RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Radioterapeuta",
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
        label="Radioterapeuta",
    )

    physicist = ModelChoiceField(
        queryset = Physicist.objects.all(),
        widget = RelatedModelWrapper(
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

    dosimetrist = ModelChoiceField(
        queryset = Dosimetrist.objects.all(),
        widget = RelatedModelWrapper(
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

    Technic = ModelChoiceField(
        queryset = Technic.objects.all(),
        widget = RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Técnico",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Técnico",
    )

    central_cons_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de consulta Central",
    )

    new_cases_cons_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de consulta Casos Nuevos",
    )

    first_stage_simulation_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de Simulación 1ra Fase",
    )

    second_stage_simulation_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de Simulación 2da Fase",
    )

    tac_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de TAC",
    )

    paint_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de Pintado",
    )

    planing_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha de Planificado",
    )

    first_stage_treatment_start_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha inicio tratamiento 1ra Fase",
    )

    second_stage_treatment_start_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "type": "date",}, format="%Y-%m-%d"),
        required=False,
        label="Fecha inicio tratamiento 2da Fase",
    )

    registered_by = CharField(
        widget = TextInput(attrs={"class": "form-control", "placeholder": "Registrado por"}),
        label = "Registrado por"
    )

    class Meta:
        model = GeneralDatasheet
        fields = "__all__"