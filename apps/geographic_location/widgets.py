from django_select2.forms import ModelSelect2Widget


class ProvinceWidget(ModelSelect2Widget):
    """Widget to search and select related province."""

    search_fields = [
        "name__trigram_similar",
    ]


class MunicipalityWidget(ModelSelect2Widget):
    """Widget to search and select related Municipality."""

    search_fields = [
        "name__icontains",
    ]
