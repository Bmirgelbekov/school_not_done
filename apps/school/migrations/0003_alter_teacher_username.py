# Generated by Django 4.2.2 on 2023-06-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]