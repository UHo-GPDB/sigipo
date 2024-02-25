from django.shortcuts import render

from apps.radiotherapy.models import (
    Dosimetrist,
    Physicist,
    TACRequest,
    Technic,
    Disease,
    Treatment,
    GeneralDatasheet,
)

from apps.radiotherapy.forms import (
    DosimetristForm,
    PhysicistForm,
    TACRequestForm,
    TechnicForm,
    DiseaseForm,
    TreatmentForm,
    GeneralDatasheetForm,
)

from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)

# * Physicist Views
class PhysicistCreateView(BaseCreateView):
    """View to handle Scheme creation."""

    model = Physicist
    form_class = PhysicistForm
    success_url = reverse_lazy("radiotherapy:physicist_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:physicist_list"

class PhysicistDetailView(BaseDetailView):
    """View to handle Physicist details."""

    model = Physicist
    form_class = PhysicistForm
    cancel_url = "radiotherapy:physicist_list"
    object_not_found_error_message = "Físico no encontrado"

class PhysicistUpdateView(BaseUpdateView):
    """View to handle Physicist edition."""

    model = Physicist
    form_class = PhysicistForm
    success_url = reverse_lazy("radiotherapy:physicist_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:physicist_list"
    object_not_found_error_message = "Físico no encontrado"

class PhysicistDeleteView(BaseDeleteView):
    """View to handle Physicist delete."""

    model = Physicist
    success_url = reverse_lazy("radiotherapy:physicist_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:physicist_list"
    object_not_found_error_message = "Físico no encontrado"

# * Dosimetrist Views
class DosimetristCreateView(BaseCreateView):
    """View to handle Dosimetrist creation."""

    model = Dosimetrist
    form_class = DosimetristForm
    success_url = reverse_lazy("radiotherapy:dosimetrist_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:dosimetrist_list"

class DosimetristDetailView(BaseDetailView):
    """View to handle Dosimetrist details."""

    model = Dosimetrist
    form_class = DosimetristForm
    cancel_url = "radiotherapy:dosimetrist_list"
    object_not_found_error_message = "Dosimetrista no encontrado"

class DosimetristUpdateView(BaseUpdateView):
    """View to handle Dosimetrist edition."""

    model = Dosimetrist
    form_class = DosimetristForm
    success_url = reverse_lazy("radiotherapy:dosimetrist_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:dosimetrist_list"
    object_not_found_error_message = "Dosimetrista no encontrado"

class DosimetristDeleteView(BaseDeleteView):
    """View to handle Dosimetrist delete."""

    model = Dosimetrist
    success_url = reverse_lazy("radiotherapy:dosimetrist_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:dosimetrist_list"
    object_not_found_error_message = "Dosimetrista no encontrado"

# * TACRequest Views
class TACRequestCreateView(BaseCreateView):
    """View to handle TACRequest creation."""

    model = TACRequest
    form_class = TACRequestForm
    success_url = reverse_lazy("radiotherapy:tac_list")
    success_message = "%(id_code)s guardado correctamente."
    cancel_url = "radiotherapy:tac_list"

class TACRequestDetailView(BaseDetailView):
    """View to handle TACRequest details."""

    model = TACRequest
    form_class = TACRequestForm
    cancel_url = "radiotherapy:tac_list"
    object_not_found_error_message = "Solicitud de TAC no encontrada"

class TACRequestUpdateView(BaseUpdateView):
    """View to handle TACRequest edition."""

    model = TACRequest
    form_class = TACRequestForm
    success_url = reverse_lazy("radiotherapy:tac_list")
    success_message = "%(id_code)s guardado correctamente."
    cancel_url = "radiotherapy:tac_list"
    object_not_found_error_message = "Solicitud de TAC no encontrada"

class TACRequestDeleteView(BaseDeleteView):
    """View to handle TACRequest delete."""

    model = TACRequest
    success_url = reverse_lazy("radiotherapy:tac")
    success_message = "%(id_code)s eliminado correctamente."
    cancel_url = "radiotherapy:tac"
    object_not_found_error_message = "Solicitud de TAC no encontrada"

# * Technic Views
class TechnicCreateView(BaseCreateView):
    """View to handle Technic creation."""

    model = Technic
    form_class = TechnicForm
    success_url = reverse_lazy("radiotherapy:technic_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:technic_list"

class TechnicDetailView(BaseDetailView):
    """View to handle Technic details."""

    model = Technic
    form_class = TechnicForm
    cancel_url = "radiotherapy:technic_list"
    object_not_found_error_message = "Técnico no encontrado"

class TechnicUpdateView(BaseUpdateView):
    """View to handle Technic edition."""

    model = Technic
    form_class = TechnicForm
    success_url = reverse_lazy("radiotherapy:technic_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:technic_list"
    object_not_found_error_message = "Técnico no encontrado"

class TechnicDeleteView(BaseDeleteView):
    """View to handle Technic delete."""

    model = Technic
    success_url = reverse_lazy("radiotherapy:technic_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:technic_list"
    object_not_found_error_message = "Técnico no encontrado"

# * Disease Views
class DiseaseCreateView(BaseCreateView):
    """View to handle Disease creation."""

    model = Disease
    form_class = DiseaseForm
    success_url = reverse_lazy("radiotherapy:disease_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:disease_list"

class DiseaseDetailView(BaseDetailView):
    """View to handle Disease details."""

    model = Disease
    form_class = DiseaseForm
    cancel_url = "radiotherapy:disease_list"
    object_not_found_error_message = "Enfermedad no encontrada"

class DiseaseUpdateView(BaseUpdateView):
    """View to handle Disease edition."""

    model = Disease
    form_class = DiseaseForm
    success_url = reverse_lazy("radiotherapy:disease_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:disease_list"
    object_not_found_error_message = "Enfermedad no encontrada"

class DiseaseDeleteView(BaseDeleteView):
    """View to handle Disease delete."""

    model = Disease
    success_url = reverse_lazy("radiotherapy:disease_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:disease_list"
    object_not_found_error_message = "Enfermedad no encontrada"

# * Treatment Views
class TreatmentCreateView(BaseCreateView):
    """View to handle Treatment creation."""

    model = Treatment
    form_class = TreatmentForm
    success_url = reverse_lazy("radiotherapy:treatment_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:treatment_list"

class TreatmentDetailView(BaseDetailView):
    """View to handle Treatment details."""

    model = Treatment
    form_class = TreatmentForm
    cancel_url = "radiotherapy:treatment_list"
    object_not_found_error_message = "Tratamiento no encontrado"

class TreatmentUpdateView(BaseUpdateView):
    """View to handle Treatment edition."""

    model = Treatment
    form_class = TreatmentForm
    success_url = reverse_lazy("radiotherapy:treatment_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:treatment_list"
    object_not_found_error_message = "Tratamiento no encontrado"

class TreatmentDeleteView(BaseDeleteView):
    """View to handle Treatment delete."""

    model = Treatment
    success_url = reverse_lazy("radiotherapy:treatment_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:treatment_list"
    object_not_found_error_message = "Tratamiento no encontrado"

# * GeneralDatasheet Views
class GeneralDatasheetCreateView(BaseCreateView):
    """View to handle General Datasheet creation."""

    model = GeneralDatasheet
    form_class = GeneralDatasheetForm
    success_url = reverse_lazy("radiotherapy:gd_list")
    success_message = "%(id_code)s guardado correctamente."
    cancel_url = "radiotherapy:gd_list"

class GeneralDatasheetDetailView(BaseDetailView):
    """View to handle General Datasheet details."""

    model = GeneralDatasheet
    form_class = GeneralDatasheetForm
    cancel_url = "radiotherapy:gd_list"
    object_not_found_error_message = "Hoja de Datos Generales no encontrada"

class GeneralDatasheetUpdateView(BaseUpdateView):
    """View to handle General Datasheet edition."""

    model = GeneralDatasheet
    form_class = GeneralDatasheetForm
    success_url = reverse_lazy("radiotherapy:gd_list")
    success_message = "%(id_code)s guardado correctamente."
    cancel_url = "radiotherapy:gd_list"
    object_not_found_error_message = "Hoja de Datos Generales no encontrada"

class GeneralDatasheetDeleteView(BaseDeleteView):
    """View to handle General Datasheet delete."""

    model = GeneralDatasheet
    success_url = reverse_lazy("radiotherapy:gd_list")
    success_message = "%(id_code)s eliminado correctamente."
    cancel_url = "radiotherapy:gd_list"
    object_not_found_error_message = "Hoja de Datos Generales no encontrada"
    