from django.contrib.admin import ModelAdmin, register

from apps.radiotherapy.models import (
    Disease,
    Dosimetrist,
    GeneralDatasheet,
    Physicist,
    TACRequest,
    Technic,
    Treatment,
)

# Register your models here.


@register(Physicist)
class PhysicistAdmin(ModelAdmin):
    """
    Physicist Django Admin view.
    """

    pass


@register(Dosimetrist)
class DosimetristAdmin(ModelAdmin):
    """
    Dosimetrist Django Admin view.
    """

    pass


@register(Technic)
class TechnicAdmin(ModelAdmin):
    """
    Technic Django Admin view.
    """

    pass


@register(TACRequest)
class TACRequestAdmin(ModelAdmin):
    """
    TACRequest Django Admin view.
    """

    pass


@register(Disease)
class DiseaseAdmin(ModelAdmin):
    """
    Disease Django Admin view.
    """

    pass


@register(Treatment)
class TreatmentAdmin(ModelAdmin):
    """
    Treatment Django Admin view.
    """

    pass


@register(GeneralDatasheet)
class GeneralDatasheetAdmin(ModelAdmin):
    """
    General Datasheet Django Admin view.
    """

    pass
