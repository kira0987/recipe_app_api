"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import forms, models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for the custom User model using BaseUserAdmin.

    Uses custom forms that work with the email-based User model.
    """

    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.User
    list_display = ("email", "name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ("email",)
    search_fields = ("email", "name")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                # "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    readonly_fields = ["last_login"]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
