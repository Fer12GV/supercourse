from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework import status
from django.db import IntegrityError
from apps.course.models import Teacher, Student, Course, Tuition, Qualification
from .serializers import (
    TeacherSerializer,
    StudentSerializer,
    CourseSerializer,
    TuitionSerializer,
    QualificationSerializer
)
from ...log.models import ExceptionLog


class CustomPagination(PageNumberPagination):
    page_size = 100000
    page_size_query_param = 'page_size'
    max_page_size = 100000

    def get_paginated_response(self, data):
        if self.get_next_link():
            next_page = self.page.number + 1
        else:
            next_page = 0

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next_link', self.get_next_link()),
            ('previous_link', self.get_previous_link()),
            ('next', next_page),
            ('previous', self.page.number - 1),
            ('pages', self.page.paginator.num_pages),
            ('page_size', self.page_size),
            ('current', self.page.number),
            ('results', data)
        ]))


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            teacher = serializer.instance
            message = f"The teacher {teacher.name} {teacher.last_name} was created successful with document " \
                      f"{teacher.document}"
            return Response({"message": message, 'success': True}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            log = ExceptionLog(name="TeacherViewSet", path="apps/course/api/viewset.py", message=e)
            log.save()
            error_message = "The Teacher already exits"
            return Response({"error": error_message, 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log = ExceptionLog(name="TeacherViewSet", path="apps/course/api/viewset.py", message=e)
            log.save()
            error_message = "The Teacher creation process has filed"
            return Response({"error": error_message, 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        serializer = None
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            teacher = serializer.instance
            message = f"The teacher {teacher.name} {teacher.last_name} was updated successful with document " \
                      f"{teacher.document}"
            response_data = {
                'success': True,
                'message': message,
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            log = ExceptionLog(name="TeacherViewSet", path="apps/course/api/viewset.py", message=e)
            log.save()
            error_message = "Teacher update process has filed"
            response_data = {
                'success': False,
                'message': error_message,
                'data': serializer.data if serializer is not None else {}
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            message = 'The teacher has been successfully deleted.'
            response_data = {
                'success': True,
                'message': message
            }
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            log = ExceptionLog(name="TeacherViewSet", path="apps/course/api/viewset.py", message=e)
            log.save()
            message = 'Teacher delete process has filed.'
            response_data = {
                'success': False,
                'message': message
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer


class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
