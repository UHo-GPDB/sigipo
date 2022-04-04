from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView


class PaginationFilterView(LoginRequiredMixin, FilterView):
    """FilterView with pagination."""

    paginate_by = 30
    extra_context: dict = None

    def get_context_data(self, *args, **kwargs) -> dict:
        """
        Save the url lookup filters to use it in the url links.
        <a href="?page={{ page_obj.next_page_number }}&{{ parameters }}">
            Next
        </a>
        """
        _request_copy = self.request.GET.copy()
        _request_copy.__mutable = True
        parameters = _request_copy.pop("page", True) and _request_copy.urlencode()
        context = super().get_context_data(*args, **kwargs)
        context["parameters"] = parameters
        num_pages = context["paginator"].num_pages
        current_page = context["page_obj"].number
        context["pagination_range"] = [
            page_number
            for page_number in range(current_page - 2, current_page + 2)
            if page_number >= 1 and page_number <= num_pages
        ]
        context |= self.extra_context
        return context


class CancelUrlMixin:
    """Mixin to add cancel url to django generics views."""

    cancel_url = None

    def get_context_data(self, *args, **kwargs) -> dict:
        """Adds given url to the context."""
        context = super().get_context_data(*args, **kwargs)
        context["cancel_url"] = self.cancel_url
        return context

    def get_cancel_url(self):
        """Returns cancel url."""
        return reverse_lazy(self.cancel_url)


class ViewTitleMixin:
    """Mixin to view title to django generics views."""

    title = None

    def get_context_data(self, *args, **kwargs) -> dict:
        """Adds given title to the context."""
        context = super().get_context_data(*args, **kwargs)
        context["view_title"] = self.title
        return context


class GetObjectErrorMixin:
    """Generate user friendly message for object not found exception."""

    object_not_found_error_message = None

    def get(self, request: HttpRequest, *args, **kwargs):
        """Override get_object to handle object not found exception."""
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, self.object_not_found_error_message)
            return redirect(self.get_cancel_url())
        return super().get(request, *args, **kwargs)


class BaseCreateView(
    LoginRequiredMixin, SuccessMessageMixin, CancelUrlMixin, ViewTitleMixin, CreateView
):
    """Base create view."""

    template_name = "base_crud/base_create.html"


class BaseUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    GetObjectErrorMixin,
    CancelUrlMixin,
    ViewTitleMixin,
    UpdateView,
):
    """Base update view."""

    template_name = "base_crud/base_update.html"


class BaseDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    GetObjectErrorMixin,
    CancelUrlMixin,
    ViewTitleMixin,
    DeleteView,
):
    """Base delete view."""

    template_name = "base_crud/base_delete.html"

    def delete(self, request: HttpRequest, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        try:
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.delete()
            success_message = self.get_success_message(self.object)
            messages.success(self.request, success_message)
            return redirect(success_url)
        except Http404:
            messages.error(self.request, self.object_not_found_error_message)
