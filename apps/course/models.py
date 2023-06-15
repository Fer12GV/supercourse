from django.db import models

from apps.course.choices import GENDER_CHOICES
from apps.accounts.choices import IDENTIFICATION_CHOICES


class Teacher(models.Model):
    type = models.CharField(max_length=2, choices=IDENTIFICATION_CHOICES)
    document = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    career = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.document} {self.name} {self.last_name}"


class Student(models.Model):
    type = models.CharField(max_length=2, choices=IDENTIFICATION_CHOICES)
    document = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.document} {self.name} {self.last_name}"


class Course(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    fk_teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE)
    fk_student = models.ManyToManyField('Student', through='Tuition')

    def __str__(self):
        return f"{self.code} {self.name}"


class Tuition(models.Model):
    code = models.CharField(max_length=255, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    hours = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    fk_student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.fk_student.name} {self.fk_course.name}"


class Qualification(models.Model):
    qualification = models.FloatField(null=True)
    fk_teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE)
    fk_student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.qualification}"
