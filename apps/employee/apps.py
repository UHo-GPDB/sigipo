from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    """Employee Config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.employee"
    verbose_name = "Empleados"
