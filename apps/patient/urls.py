from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.patient.filters import NuclearMedicinePatientFilter, PatientFilter
from apps.patient.models import Patient
from apps.patient.views import (
    NuclearMedicinePatientCreateView,
    NuclearMedicinePatientDeleteView,
    NuclearMedicinePatientDetailView,
    NuclearMedicinePatientUpdateView,
    PatientChangeStatus,
    PatientCreateView,
    PatientDeleteView,
    PatientDetailView,
    PatientUpdateView,
    check_patient_created,
    patient_download_table,
)

app_name = "patient"

urlpatterns = [
    # * Patient URLs
    path(
        "oncologic/list/",
        PaginationFilterView.as_view(
            model=Patient,
            filterset_class=PatientFilter,
            extra_context={
                "add_url": "patient:oncologic_create",
                "detail_url": "patient:oncologic_detail",
                "edit_url": "patient:oncologic_update",
                "delete_url": "patient:oncologic_delete",
            },
            permission_required="patient:view_oncologic",
            queryset=Patient.objects.only_oncologic(),
            post_function=patient_download_table,
        ),
        name="oncologic_list",
    ),
    path(
        "oncologic/create/",
        PatientCreateView.as_view(),
        name="oncologic_create",
    ),
    path(
        "oncologic/detail/<pk>/",
        PatientDetailView.as_view(),
        name="oncologic_detail",
    ),
    path(
        "oncologic/update/<pk>/",
        PatientUpdateView.as_view(),
        name="oncologic_update",
    ),
    path(
        "oncologic/delete/<pk>/",
        PatientDeleteView.as_view(),
        name="oncologic_delete",
    ),
    path(
        "change_status/",
        PatientChangeStatus.as_view(),
        name="oncologic_change_status",
    ),
    path(
        "change_status/<pk>/",
        PatientChangeStatus.as_view(),
        name="oncologic_change_status_confirmation",
    ),
    # * Nuclear Medicine Patient URLs
    path(
        "patient/list/",
        PaginationFilterView.as_view(
            model=Patient,
            filterset_class=NuclearMedicinePatientFilter,
            queryset=Patient.objects.all(),
            template_name_suffix="_no_oncologic_filter",
            post_function=patient_download_table,
        ),
        name="patient_list",
    ),
    getUrl(NuclearMedicinePatientCreateView),
    getUrl(NuclearMedicinePatientDetailView),
    getUrl(NuclearMedicinePatientUpdateView),
    getUrl(NuclearMedicinePatientDeleteView),
    path(
        "check_patient_created/<pk>/",
        check_patient_created,
        name="check_patient_created",
    ),
]
