from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Student
from .forms import TeacherRegistrationForm, TeacherLoginForm, StudentForm


def index(request):
    return render(request, 'index.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})





def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'register_teacher.html', {'form': form})

def login_teacher(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_list')  
            else:
                form.add_error(None, 'Неверный номер телефона или пароль.')
    else:
        form = TeacherLoginForm()
    return render(request, 'login_teacher.html', {'form': form})