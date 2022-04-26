from django.urls import path

from apps.core.views import PaginationFilterView
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
                "crud_name": "Pacientes",
                "crud_instance_name": "paciente",
                "add_url": "patient:oncologic_create",
                "detail_url": "patient:oncologic_detail",
                "edit_url": "patient:oncologic_update",
                "delete_url": "patient:oncologic_delete",
            },
            queryset=Patient.objects.only_oncologic(),
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
            extra_context={
                "crud_name": "Pacientes",
                "crud_instance_name": "paciente",
                "add_url": "patient:patient_create",
                "detail_url": "patient:patient_detail",
                "edit_url": "patient:patient_update",
                "delete_url": "patient:patient_delete",
            },
            queryset=Patient.objects.all(),
        ),
        name="patient_list",
    ),
    path(
        "patient/create/",
        NuclearMedicinePatientCreateView.as_view(),
        name="patient_create",
    ),
    path(
        "patient/detail/<pk>/",
        NuclearMedicinePatientDetailView.as_view(),
        name="patient_detail",
    ),
    path(
        "patient/update/<pk>/",
        NuclearMedicinePatientUpdateView.as_view(),
        name="patient_update",
    ),
    path(
        "patient/delete/<pk>/",
        NuclearMedicinePatientDeleteView.as_view(),
        name="patient_delete",
    ),
]
