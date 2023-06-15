from django.contrib import admin

from apps.course.models import Teacher, Student, Course, Tuition, Qualification


class Teacher_Admin(admin.ModelAdmin):
    list_display = ['pk', 'type', 'document', 'name', 'last_name', 'gender', 'career', 'age', 'address', 'email']
    search_fields = ['document', 'name', 'last_name', 'email']
    list_filter = ['document', 'name', 'last_name', 'gender', 'career', 'age', 'address', 'city', 'country',
                   'is_virtual']
    list_per_page = 100


class Student_Admin(admin.ModelAdmin):
    list_display = ['pk', 'type', 'document', 'name', 'last_name', 'gender', 'age', 'address', 'email']
    search_fields = ['document', 'name', 'last_name', 'email']
    list_filter = ['document', 'name', 'last_name', 'gender', 'age', 'address', 'city', 'country', 'is_virtual']
    list_per_page = 100


class Course_Admin(admin.ModelAdmin):
    raw_id_fields = ('fk_teacher',)
    autocomplete_fields = ('fk_student',)
    list_display = ['pk', 'code', 'name', 'description', 'fk_teacher']
    search_fields = ['code', 'name']
    list_filter = ['code', 'name', 'fk_teacher', 'fk_student']
    list_per_page = 100


class Tuition_Admin(admin.ModelAdmin):
    raw_id_fields = ('fk_student', 'fk_course',)
    list_display = ['code', 'registration_date', 'start_date', 'end_date', 'hours', 'price', 'fk_student', 'fk_course']
    search_fields = ['code', 'registration_date', 'start_date']
    list_filter = ['code', 'registration_date', 'start_date']
    list_per_page = 100


class Qualification_Admin(admin.ModelAdmin):
    raw_id_fields = ('fk_teacher', 'fk_student', 'fk_course',)
    list_display = ['qualification', 'fk_teacher', 'fk_student', 'fk_course']
    search_fields = ['qualification']
    list_filter = ['qualification', 'fk_teacher', 'fk_student', 'fk_course']
    list_per_page = 100


admin.site.register(Teacher, Teacher_Admin)
admin.site.register(Student, Student_Admin)
admin.site.register(Course, Course_Admin)
admin.site.register(Tuition, Tuition_Admin)
admin.site.register(Qualification, Qualification_Admin)
