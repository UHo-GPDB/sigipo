from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from apps.geographic_location.models import Municipality, Province, Location


class ProvinceFilter(FilterSet):
    """Filters to search for provinces."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Province
        fields = [
            "name",
        ]


class MunicipalityFilter(FilterSet):
    """Filters to search for municipalities."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )
    province = CharFilter(
        lookup_expr="name__icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Provincia contiene"}
        ),
    )

    class Meta:
        model = Municipality
        fields = [
            "name",
            "province",
        ]

class LocationFilter(FilterSet):
    """Filters to search for Localities."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    municipality = CharFilter(
        lookup_expr="name__icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Municipio contiene"}
        ),
    )

    province = CharFilter(
        lookup_expr="name__icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Provincia contiene"}
        ),
    )

    class Meta:
        model = Location
        fields = [
            "name",
            "municipality",
            "province",
        ]