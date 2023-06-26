from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class School(models.Model):
    name = models.CharField(max_length=100)
    classes = models.CharField(max_length=4)


class Classes(models.Model):
    name = models.CharField(max_length=5)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='classes')




class Teacher(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=50)


class Student(models.Model):
    GENDERS = (
        ('male', 'мужской'),
        ('female', 'женский')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    classs = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='students')
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=7, choices=GENDERS)
    photo = models.ImageField(upload_to='student_photos', null=True, blank=True)


@receiver(post_save, sender=Student)
def send_mail_to_student(sender: Student, instance: Student, created: bool, **kwargs):
    if created:
        subject = 'Добро пожаловать!'
        message = f'Привет, {instance.name}! Добро пожаловать в нашу школу!'
        from_mail = 'pythonmailsender007@gmail.com'
        to_email = instance.email
        send_mail(
            subject=subject, 
            message=message, 
            from_email=from_mail,
            recipient_list=[to_email])