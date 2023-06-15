from django.contrib import admin

from apps.course.models import Teacher


class Teacher_Admin(admin.ModelAdmin):
    list_display = ['pk', 'type', 'document', 'name', 'last_name', 'gender', 'career', 'age', 'address', 'email']
    search_fields = ['document', 'name', 'last_name', 'email']
    list_filter = ['document', 'name', 'last_name', 'gender', 'career', 'age', 'address']
    list_per_page = 100


admin.site.register(Teacher, Teacher_Admin)
