from django.urls import reverse_lazy

from apps.core.views import BaseCreateView, BaseUpdateView
from apps.geographic_location.forms import ProvinceForm
from apps.geographic_location.models import Province


class ProvinceCreateView(BaseCreateView):
    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"
    title = "Añadir provincia"


class ProvinceUpdateView(BaseUpdateView):
    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"
    title = "Editar provincia"
