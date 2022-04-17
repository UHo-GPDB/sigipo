import json
import os

from django.conf import settings
from django.db.models import Case, Count, F, Value, When
from django.http import JsonResponse
from django.views.generic import TemplateView

from apps.patient.models import Patient

MATCH_PROVINCE_CODE = Case(
    When(province_name="Pinar del Río", then=Value("cu-pr")),
    When(province_name="La Habana", then=Value("cu-ch")),
    When(province_name="Artemisa", then=Value("cu-ar")),
    When(province_name="Mayabeque", then=Value("cu-mq")),
    When(province_name="Matanzas", then=Value("cu-ma")),
    When(province_name="Villa Clara", then=Value("cu-vc")),
    When(province_name="Cienfuegos", then=Value("cu-cf")),
    When(province_name="Sancti Spíritus", then=Value("cu-ss")),
    When(province_name="Ciego de Ávila", then=Value("cu-ca")),
    When(province_name="Camagüey", then=Value("cu-cm")),
    When(province_name="Las Tunas", then=Value("cu-lt")),
    When(province_name="Holguín", then=Value("cu-ho")),
    When(province_name="Granma", then=Value("cu-gr")),
    When(province_name="Santiago de Cuba", then=Value("cu-sc")),
    When(province_name="Guantánamo", then=Value("cu-gu")),
    When(province_name="Isla de la Juventud", then=Value("cu-ij")),
)


class Dashboard(TemplateView):
    """View to handle dashboard."""

    template_name = "dashboard/dashboard.html"

    def get(self, request, *args, **kwargs):
        match request.GET.get("data"):
            case "county":
                with open(
                    os.path.join(
                        settings.BASE_DIR,
                        "sigipo",
                        "static",
                        "json",
                        "cu-all.topo.json",
                    )
                ) as file:
                    file = json.load(file)
                return JsonResponse(data=file)
            case "born":
                data = list(
                    Patient.objects.only_oncologic()
                    .annotate(province_name=F("born_municipality__province__name"))
                    .values("province_name")
                    .order_by("province_name")
                    .annotate(
                        province_code=MATCH_PROVINCE_CODE,
                        count=Count("pk"),
                    )
                    .values_list("province_code", "count")
                )
                return JsonResponse(data=data, safe=False)
            case "residence":
                data = list(
                    Patient.objects.only_oncologic()
                    .annotate(province_name=F("residence_municipality__province__name"))
                    .values("province_name")
                    .order_by("province_name")
                    .annotate(
                        province_code=MATCH_PROVINCE_CODE,
                        count=Count("pk"),
                    )
                    .values_list("province_code", "count")
                )
                return JsonResponse(data=data, safe=False)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)