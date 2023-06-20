from rest_framework import serializers

from apps.accounts.choices import IDENTIFICATION_CHOICES
from apps.course.api.aux_core.choicefield import ChoiceTypeField, ChoiceGenderField
from apps.course.choices import GENDER_CHOICES
from apps.course.models import Teacher, Student, Course, Tuition, Qualification


class TeacherSerializer(serializers.ModelSerializer):
    type = ChoiceTypeField(choices=IDENTIFICATION_CHOICES, required=True)
    document = serializers.CharField(required=True, max_length=255)
    name = serializers.CharField(required=True, max_length=255)
    last_name = serializers.CharField(required=True, max_length=255)
    gender = ChoiceGenderField(choices=GENDER_CHOICES, required=True)
    career = serializers.CharField(required=True, max_length=255)
    age = serializers.IntegerField(required=True)
    address = serializers.CharField(allow_blank=True, required=False)
    email = serializers.EmailField(required=True)
    city = serializers.CharField(allow_blank=True,required=False, max_length=255)
    country = serializers.CharField(allow_blank=True,required=False, max_length=255)
    is_virtual = serializers.BooleanField(required=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def validate_age(self, value):
        if value is not None and value < 18:
            raise serializers.ValidationError("The age must be greater than 18 years old.")
        return value


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'
