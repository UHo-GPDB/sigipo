from django.forms import TextInput, Select
from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter, ChoiceFilter
from django_select2.forms import ModelSelect2Widget

from apps.geographic_location.models import Municipality
from apps.death_certificate.models import DeathCertificate, ConfirmationCausesChoices


class DeathCertificateFilter(FilterSet):
    """Filters to search for death certificates."""

    time_of_death = DateFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Fecha de Fallecimiento"}
        ),
        label="Fecha de Fallecimiento",
    )

    deathCertificate_number = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Número de Certificación de Defunción"}
        ),
        label="Número de Certificación de Defunción",
    )

    first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
        label="Nombre",
    )

    last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos"}
        ),
        label="Apellidos",
    )

    ConfirmationCauses = ChoiceFilter(
        choices=ConfirmationCausesChoices.choices,
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Confirmación de las causas"}
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
                "name__icontains",
                "province__name__icontains",
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
                "name__icontains",
                "province__name__icontains",
            ],
        ),
        label="Municipio natal",
    )
    class Meta:
        model = DeathCertificate
        fields = [
            "deathCertificate_number",
            "time_of_death",
            "first_name",
            "last_name",
            "ConfirmationCauses",
            "residence_municipality",
            "born_municipality",

        ]
