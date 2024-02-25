from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.radiotherapy.filters import (
    DiseaseFilter,
    DosimetristFilter,
    GeneralDatasheetFilter,
    PhysicistFilter,
    TACRequestFilter,
    TechnicFilter,
    TreatmentFilter,
)
from apps.radiotherapy.models import (
    Disease,
    Dosimetrist,
    GeneralDatasheet,
    Physicist,
    TACRequest,
    Technic,
    Treatment,
)
from apps.radiotherapy.views import (
    DiseaseCreateView,
    DiseaseDeleteView,
    DiseaseDetailView,
    DiseaseUpdateView,
    DosimetristCreateView,
    DosimetristDeleteView,
    DosimetristDetailView,
    DosimetristUpdateView,
    GeneralDatasheetCreateView,
    GeneralDatasheetDeleteView,
    GeneralDatasheetDetailView,
    GeneralDatasheetUpdateView,
    PhysicistCreateView,
    PhysicistDeleteView,
    PhysicistDetailView,
    PhysicistUpdateView,
    TACRequestCreateView,
    TACRequestDeleteView,
    TACRequestDetailView,
    TACRequestUpdateView,
    TechnicCreateView,
    TechnicDeleteView,
    TechnicDetailView,
    TechnicUpdateView,
    TreatmentCreateView,
    TreatmentDeleteView,
    TreatmentDetailView,
    TreatmentUpdateView,
)

app_name = "radiotherapy"
urlpatterns = [
    # Physicist URLs
    path(
        "physicist/list/",
        PaginationFilterView.as_view(
            model=Physicist,
            filterset_class=PhysicistFilter,
        ),
        name="physicist_list",
    ),
    getUrl(PhysicistCreateView),
    getUrl(PhysicistDetailView),
    getUrl(PhysicistUpdateView),
    getUrl(PhysicistDeleteView),
    # Dosimetrist URLs
    path(
        "dosimetrist/list/",
        PaginationFilterView.as_view(
            model=Dosimetrist,
            filterset_class=DosimetristFilter,
        ),
        name="dosimetrist_list",
    ),
    getUrl(DosimetristCreateView),
    getUrl(DosimetristDetailView),
    getUrl(DosimetristUpdateView),
    getUrl(DosimetristDeleteView),
    # TACRequest URLs
    path(
        "tacrequest/list/",
        PaginationFilterView.as_view(
            model=TACRequest,
            filterset_class=TACRequestFilter,
        ),
        name="tac_list",
    ),
    getUrl(TACRequestCreateView),
    getUrl(TACRequestDetailView),
    getUrl(TACRequestUpdateView),
    getUrl(TACRequestDeleteView),
    # Technic URLs
    path(
        "technic/list/",
        PaginationFilterView.as_view(
            model=Technic,
            filterset_class=TechnicFilter,
        ),
        name="technic_list",
    ),
    getUrl(TechnicCreateView),
    getUrl(TechnicDetailView),
    getUrl(TechnicUpdateView),
    getUrl(TechnicDeleteView),
    # Disease URLs
    path(
        "disease/list/",
        PaginationFilterView.as_view(
            model=Disease,
            filterset_class=DiseaseFilter,
        ),
        name="disease_list",
    ),
    getUrl(DiseaseCreateView),
    getUrl(DiseaseDetailView),
    getUrl(DiseaseUpdateView),
    getUrl(DiseaseDeleteView),
    # Treatment URLs
    path(
        "treatment/list/",
        PaginationFilterView.as_view(
            model=Treatment,
            filterset_class=TreatmentFilter,
        ),
        name="treatment_list",
    ),
    getUrl(TreatmentCreateView),
    getUrl(TreatmentDetailView),
    getUrl(TreatmentUpdateView),
    getUrl(TreatmentDeleteView),
    # General Datasheets URLs
    path(
        "generalDatasheet/list/",
        PaginationFilterView.as_view(
            model=GeneralDatasheet,
            filterset_class=GeneralDatasheetFilter,
        ),
        name="gd_list",
    ),
    getUrl(GeneralDatasheetCreateView),
    getUrl(GeneralDatasheetDetailView),
    getUrl(GeneralDatasheetUpdateView),
    getUrl(GeneralDatasheetDeleteView),
]
