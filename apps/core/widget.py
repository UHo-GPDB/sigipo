import datetime as dt
import json

from django.forms import (
    CharField,
    DateField,
    DateInput,
    MultiValueField,
    MultiWidget,
    TextInput,
)
from django.utils.dateparse import parse_datetime


class CauseOfDeathWidget(MultiWidget):
    template_name = "components/widgets/cause_of_death.html"

    def __init__(
        self,
        attrs=None,
        cause_attrs=None,
        date_attrs=None,
        code_attrs=None,
    ):
        date_input_attr = (date_attrs or {}) | {
            "type": "date",
            "label": "Fecha",
        }

        widgets = (
            TextInput(
                attrs=(cause_attrs or {})
                | {
                    "label": "Causa de muerte",
                },
            ),
            DateInput(
                attrs=date_input_attr,
                format="%Y-%m-%d",
            ),
            TextInput(
                attrs=(code_attrs or {})
                | {
                    "label": "Código",
                },
            ),
        )
        super().__init__(widgets)

    def decompress(self, value):
        if value:
            value = json.loads(value)
            cause, date, code = value.values()
            return [cause, parse_datetime(date), code]
        return [None, None, None]


class CauseOfDeathField(MultiValueField):
    widget = CauseOfDeathWidget

    def __init__(self, *arg,**kwargs):
        fields = (
            CharField(),
            DateField(),
            CharField(),
        )
        super().__init__(fields, **kwargs)

    def compress(self, data_list):
        if data_list:
            date: dt.datetime = data_list[1]
            return json.dumps(
                {
                    "cause": data_list[0],
                    "date": str(date.strftime("%Y-%m-%d")),
                    "code": data_list[2],
                }
            )
        return None
