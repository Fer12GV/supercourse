from django.db import models
from django.core.exceptions import ValidationError

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
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    is_virtual = models.BooleanField(null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower() if isinstance(self.name, str) else self.name
        self.last_name = self.last_name.lower() if isinstance(self.last_name, str) else self.last_name
        self.career = self.career.lower() if isinstance(self.career, str) else self.career
        self.address = self.address.lower() if isinstance(self.address, str) else self.address
        self.city = self.city.lower() if isinstance(self.city, str) else self.city
        self.country = self.country.lower() if isinstance(self.country, str) else self.country
        super().save(*args, **kwargs)

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
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    is_virtual = models.BooleanField(null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower() if isinstance(self.name, str) else self.name
        self.last_name = self.last_name.lower() if isinstance(self.last_name, str) else self.last_name
        self.address = self.address.lower() if isinstance(self.address, str) else self.address
        self.city = self.city.lower() if isinstance(self.city, str) else self.city
        self.country = self.country.lower() if isinstance(self.country, str) else self.country
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.document} {self.name} {self.last_name}"


class Course(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    fk_teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE)
    fk_student = models.ManyToManyField('Student', through='Tuition')

    def save(self, *args, **kwargs):
        self.name = self.name.lower() if isinstance(self.name, str) else self.name
        self.description = self.description.lower() if isinstance(self.description, str) else self.description
        super().save(*args, **kwargs)

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

    def clean(self):
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            raise ValidationError("The end date must be greater than start date.")

    class Meta:
        unique_together = ('fk_student', 'fk_course')

    def __str__(self):
        return f"{self.code}"


class Qualification(models.Model):
    qualification = models.FloatField(null=True)
    fk_teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE)
    fk_student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.qualification}"
