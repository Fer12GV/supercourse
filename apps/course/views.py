from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            msg = "Invalid username or password"
            messages.error(request, msg)
            context = {"message": msg, "show_notification": True}
            return render(request, "login.html", context)

    if not request.user.id:
        return render(request, "login.html")

    return redirect('importer')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def importer_view(request):
    return render(request, 'importer.html')


@login_required
def teacher_view(request):
    return render(request, 'teacher.html')


@login_required
def student_view(request):
    return render(request, 'student.html')


@login_required
def course_view(request):
    return render(request, 'course.html')


@login_required
def tuition_view(request):
    return render(request, 'tuition.html')


@login_required
def qualification_view(request):
    return render(request, 'qualification.html')
