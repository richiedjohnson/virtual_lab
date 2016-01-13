from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SecurityQuestion(models.Model):
    name = models.CharField(max_length=500)

class VLAB_User(AbstractBaseUser):
    email = models.EmailField('email address', unique=True, db_index=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    admitted_on = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email


class UserSecurityAnswers(models.Model):
    user = models.ForeignKey(VLAB_User, on_delete=models.CASCADE)
    question = models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

@python_2_unicode_compatible
class Course(models.Model):
    name = models.CharField(max_length=200)
    course_number = models.CharField(max_length=200)
    registration_code = models.CharField(max_length=10)
    capacity = models.IntegerField(default=0)
    students_registered = models.IntegerField(default=0)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=10)

    def has_free_slots(self):
        return self.students_registered < self.capacity

    def __str__(self):
        return self.course_number + ":" + self.name

@python_2_unicode_compatible
class Faculty(models.Model):
    PROFESSOR = 'PR'
    TEACHING_ASSISTANT = 'TA'
    TYPE_CHOICES = (
        (PROFESSOR, 'Professor'),
        (TEACHING_ASSISTANT, 'TeachingAssistant')
    )
    course = models.ForeignKey(Course)
    user_id = models.CharField(max_length=20)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=PROFESSOR)

    def __str__(self):
        return self.user_id + ":" + self.type
