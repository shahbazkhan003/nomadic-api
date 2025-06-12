from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'fullname', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'fullname', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'fullname', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    ordering = ('email',)
    search_fields = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
