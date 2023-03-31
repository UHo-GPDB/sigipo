from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import User


@register(User)
class UserAdmin(UserAdmin):
    """Custom User admin."""

    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "first_name", "last_name", "email")

