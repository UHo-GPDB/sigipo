from django.contrib.admin import ModelAdmin, register

from apps.death_certificate.models import DeathCertificate


@register(DeathCertificate)
class DeathCertificateAdmin(ModelAdmin):
    """DeathCertificate Django Admin view."""

    list_display = ("deathCertificate_number",)
    list_select_related = ("deathCertificate_number",)
    list_display_links = ("deathCertificate_number",)
