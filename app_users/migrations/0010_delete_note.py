# Generated by Django 5.0.6 on 2024-06-09 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0009_remove_student_hobbies_remove_student_teacher_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]
