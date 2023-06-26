
from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.pathologic_anathomy.forms import BiopsyRequestForm
from apps.pathologic_anathomy.models import BiopsyRequest

# Create your views here.


class BiopsyRequestCreateView(BaseCreateView):
    """View to handle BiopsyOrder view."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia guardada correctamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"


class BiopsyRequestDetailView(BaseDetailView):
    """View to handle BiopsyOrder details."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Orden de biopsia no encontrada"


class BiopsyRequestUpdateView(BaseUpdateView):
    """View to handle BiopsyOrder edition."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia guardada correctamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Biopsia no encontrada"


class BiopsyRequestDeleteView(BaseDeleteView):
    """View to handle BiopsyOrder delete."""

    model = BiopsyRequest
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia eliminada satisfactoriamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Biopsia no encontrada"

