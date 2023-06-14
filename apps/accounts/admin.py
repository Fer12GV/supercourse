from django.contrib import admin
from .models import User


class User_Admin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'type', 'document']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('type', 'document')}),
    )
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(User, User_Admin)
