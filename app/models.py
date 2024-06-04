from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from app.managers import CustomUserManager
from administrator.models import Hospital
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(default="",max_length=20)
    full_name = models.CharField(default="",max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(default=0,max_length=10, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Admission(models.Model):
    gender_type = (
        (None,"please select"),
        ("Male", "Male"),
        ("Female", "Female"),
    )

    severity = (
        (None,"please select"),
        ("High", "High"),
        ("Low", "Low"),
    )

    hospital_list = Hospital.objects.all().order_by('name')    
    state_list = set(list(hospital_list.values_list('state',flat=True)))
    city_list = set(list(hospital_list.values_list('city',flat=True)))

    state_choices = ((i,i) for i in state_list)
    city_choices = list((i,i) for i in city_list)
    patient_name = models.CharField(default="",max_length=20)
    email = models.EmailField(_('email address'))
    age = models.IntegerField(blank=True,null=True)
    phone_number = models.CharField(default=0,max_length=10)
    gender = models.CharField(max_length=20,blank=True,null=True,choices=gender_type,default=None)
    address = models.TextField(blank=True,null=True)
    relative_address = models.TextField(blank=True,null=True)
    relative_contact = models.CharField(default=0,max_length=10)
    severity = models.CharField(max_length=20,blank=True,null=True,choices=severity,default=None)
    aadhaar_number = models.CharField(default="",max_length=12)
    admission_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    user_id = models.ForeignKey("app.CustomUser", on_delete=models.CASCADE,default=None,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True,null=True,choices=state_choices,default=None)
    city = models.CharField(max_length=100,blank=True,null=True,choices=city_choices,default=None)

class HospitalPatientDetails(models.Model):
    gender_type = (
        (None,"please select"),
        ("Male", "Male"),
        ("Female", "Female"),
    )

    severity = (
        (None,"please select"),
        ("High", "High"),
        ("Low", "Low"),
    )

    bed_type = (
        (None,"please select"),
        ("With oxygen", "With oxygen"),
        ("Without oxygen", "Without oxygen"),
    )

    hospital_id = models.IntegerField(blank=True,null=True)
    username = models.CharField(default="",max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    age = models.IntegerField(blank=True,null=True)
    phone_number = models.CharField(default=0,max_length=10)
    gender = models.CharField(max_length=20,blank=True,null=True,choices=gender_type,default=None)
    address = models.TextField(blank=True,null=True)
    relative_address = models.TextField(blank=True,null=True)
    relative_contact = models.CharField(default=0,max_length=10)
    serverity = models.CharField(max_length=20,blank=True,null=True,choices=severity,default=None)
    aadhaar_number = models.CharField(default="",max_length=12)
    bed_type = models.CharField(max_length=20,blank=True,null=True,choices=bed_type,default=None)
    admission_date= models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)



class CareCenterPatientDetails(models.Model):
    gender_type = (
        (None,"please select"),
        ("Male", "Male"),
        ("Female", "Female"),
    )

    severity = (
        (None,"please select"),
        ("High", "High"),
        ("Low", "Low"),
    )

    carecenter_id = models.IntegerField(blank=True,null=True)
    username = models.CharField(default="",max_length=20)
    email = models.EmailField(_('email address'))
    age = models.IntegerField(blank=True,null=True)
    phone_number = models.CharField(default=0,max_length=10)
    gender = models.CharField(max_length=20,blank=True,null=True,choices=gender_type,default=None)
    address = models.TextField(blank=True,null=True)
    relative_address = models.TextField(blank=True,null=True)
    relative_contact = models.CharField(default=0,max_length=10)
    serverity = models.CharField(max_length=20,blank=True,null=True,choices=severity,default=None)
    aadhaar_number = models.CharField(default="",max_length=12)
    bed_type = models.CharField(max_length=20,blank=True,null=True,default="Without oxygen")
    admission_date= models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

class UserBookedAdmissionHistory(models.Model):
    admission_id = models.IntegerField(blank=True,null=True)
    user_id = models.IntegerField(blank=True,null=True)
    hospital_id = models.IntegerField(blank=True,null=True)
    carecenter_id = models.IntegerField(blank=True,null=True)