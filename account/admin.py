from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # This tells Django which fields to show when editing a user
    list_display = ('email', 'username', 'is_staff', 'is_active')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)