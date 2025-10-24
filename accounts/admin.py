from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('middle_name', 'user_role', 'balance')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_role', 'balance')
