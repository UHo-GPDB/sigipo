from typing import Final

from django_select2.forms import ModelSelect2Widget

from apps.core.functions import getUrl

REPLACE_URL_VALUE: Final[str] = "URL_VALUE_FOR_REPLACE"


class RelatedModelWrapper(ModelSelect2Widget):
    template_name = "custom_widgets/select.html"

    def __init__(self, *args, **kwargs):
        self.add_url = kwargs.pop("add_url", None)
        self.view_url = kwargs.pop("view_url", None)
        self.add_permission = kwargs.pop("add_permission", None)
        self.view_permission = kwargs.pop("view_permission", None)
        super().__init__(*args, **kwargs)

    def get_context(self, name: str, value: str, attrs: dict):
        context = super().get_context(name, value, attrs)
        model = (
            self.model or None if self.queryset is None else self.queryset.model
        ) or self.choices.queryset.model
        if self.add_url is not None and self.view_url is not None:
            self.add_url = getUrl(full_url=self.add_url)
            self.view_url = getUrl(full_url=self.view_url, value=REPLACE_URL_VALUE)
        elif model is not None:
            self.add_url = getUrl(model)
            self.view_url = getUrl(model, "detail", REPLACE_URL_VALUE)
        request = getattr(self, "request", None)
        context["add_perm"] = request.user.has_perm(self.add_permission)
        context["view_perm"] = request.user.has_perm(self.view_permission)
        context["add_url"] = self.add_url
        context["view_url"] = self.view_url
        return context
