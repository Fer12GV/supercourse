from django.contrib import admin

from apps.log.models import ExceptionLog


class ExceptionLog_Admin(admin.ModelAdmin):
    list_display = ('name', 'path', 'timestamp', 'message')
    search_fields = ('name', 'path', 'message')
    list_filter = ('timestamp',)
    readonly_fields = ('name', 'path', 'timestamp', 'message', 'history')


admin.site.register(ExceptionLog, ExceptionLog_Admin)
