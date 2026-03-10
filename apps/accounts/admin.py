from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    User is special model in django so, django provides a special admin class for it. It provides many built-in features that django already impolemented for user
    fieldsets where personal info, permission, Important dates will be in section and shown properly. This is while showing already 
    added data in the admin

    add_fieldsets= It is for the form to be nice clean while adding fields in admin
    

    """
    model = User
    list_display = ("email", "full_name", "is_staff", "is_active", "created_at")
    ordering = ("email",)
    search_fields = ("email", "full_name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name", "phone")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "phone", "password1", "password2", "is_staff", "is_active"),
        }),
    )