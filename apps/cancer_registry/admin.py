from django.contrib.admin import ModelAdmin, register

from apps.cancer_registry.models import Neoplasm


@register(Neoplasm)
class NeoplasmAdmin(ModelAdmin):
    """Neoplasm Django Admin view."""

    list_display = (
        "patient",
        "primary_site",
    )
    search_fields = (
        "patient__first_name",
        "patient__last_name",
    )
    list_select_related = (
        "patient",
        "primary_site",
        "histologic_type",
    )
    list_display_links = ("patient",)
