from django.urls import path, include
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework import routers
from apps.course.api.viewset import (
    TeacherViewSet,
    StudentViewSet,
    CourseViewSet,
    TuitionViewSet,
    QualificationViewSet
)

router = routers.DefaultRouter()
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('tuitions', TuitionViewSet)
router.register('qualifications', QualificationViewSet)

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('importer/', importer_view, name='importer'),
    path('teacher/', teacher_view, name='teacher'),
    path('student/', student_view, name='student'),
    path('tuition/', tuition_view, name='tuition'),
    path('course/', course_view, name='course'),
    path('qualification/', qualification_view, name='qualification'),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += [
    path('api/', include(router.urls)),
]
