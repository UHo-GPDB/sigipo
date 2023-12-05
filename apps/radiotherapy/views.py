from django.shortcuts import render

from apps.radiotherapy.models import (
    Dosimetrist,
    Physicist,
    TACRequest,
)

from apps.radiotherapy.forms import (
    DosimetristForm,
    PhysicistForm,
    TACRequestForm
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