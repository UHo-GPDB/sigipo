from django.urls import path

from apps.radiotherapy.models import (
    Physicist, 
    Dosimetrist, 
    TACRequest
    )
from apps.radiotherapy.views import (
    PhysicistCreateView,
    PhysicistUpdateView,
    PhysicistDetailView,
    PhysicistDeleteView,
    DosimetristCreateView,
    DosimetristDetailView,
    DosimetristUpdateView,
    DosimetristDeleteView,
    TACRequestCreateView,
    TACRequestDeleteView,
    TACRequestDetailView,
    TACRequestUpdateView,
    )

from apps.radiotherapy.filters import PhysicistFilter, DosimetristFilter

from apps.core.views import PaginationFilterView, getUrl


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
            filterset_class=DosimetristFilter,
        ),
        name="tac_list",
    ),
    getUrl(TACRequestCreateView),
    getUrl(TACRequestDetailView),
    getUrl(TACRequestUpdateView),
    getUrl(TACRequestDeleteView),
    ]