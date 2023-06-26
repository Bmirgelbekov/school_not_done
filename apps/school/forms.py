from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher, Student

class TeacherRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    username = forms.CharField(max_length=50)

    class Meta:
        model = Teacher
        fields = ('username','phone_number', 'password1', 'password2')

class TeacherLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'date_of_birth', 'classs', 'address', 'gender', 'photo')