from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email,
                    password=None):
        user = self.model(email=email, password=password)
        user.set_password(user.password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,
                         password):
        user = self.create_user(email,
                                password=password)
        user.set_password(user.password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Intake_Period(models.Model):
    period_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.period_name


class VLAB_User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True, db_index=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    admitted_on = models.ForeignKey(Intake_Period, null=True, blank=True)
    department = models.ForeignKey(Department, null=True)
    phone = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.IntegerField(null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email


class Course(models.Model):
    name = models.CharField(max_length=200)
    course_number = models.CharField(max_length=200)
    registration_code = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField(default=0)
    students_registered = models.IntegerField(default=0)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=10)

    def has_free_slots(self):
        return self.students_registered < self.capacity

    def __str__(self):
        return self.course_number + ":" + self.name


class Faculty(models.Model):
    PROFESSOR = 'PR'
    TEACHING_ASSISTANT = 'TA'
    TYPE_CHOICES = (
        (PROFESSOR, 'Professor'),
        (TEACHING_ASSISTANT, 'TeachingAssistant')
    )
    course = models.ForeignKey(Course)
    user = models.OneToOneField(VLAB_User, null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=PROFESSOR)

    def __str__(self):
        return self.user_id + ":" + self.type


class Registered_Courses(models.Model):
    student = models.ForeignKey(VLAB_User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course)
    registered_date = models.DateTimeField(default=datetime.now, blank=True)


class Audit(models.Model):
    done_by = models.IntegerField()
    done_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=100)
    item_id = models.IntegerField()
    action = models.CharField(max_length=500)
