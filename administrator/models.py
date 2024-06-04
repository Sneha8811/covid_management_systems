from django.db import models
from datetime import datetime
from django.utils import timezone

class Hospital(models.Model):
    Hospital_type_CHOICES = (
    (None,"please select"),
    ("Private", "Private"),
    ("Government", "Government"),
)
    name = models.CharField(max_length=250,blank=True,null=True)
    hospital_type = models.CharField(max_length=20,blank=True,null=True,choices=Hospital_type_CHOICES,default=None)
    state = models.CharField(max_length=250,blank=True,null=True)
    city = models.CharField(max_length=250,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    created = models.DateField(default=timezone.now,null=True, blank=True)
    updated = models.DateField(default=timezone.now,null=True, blank=True)
    description = models.TextField(blank=True,null=True)
  
    def __str__(self):
        return self.name


class Carecenter(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True)
    state = models.CharField(max_length=250,blank=True,null=True)
    city = models.CharField(max_length=250,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    created = models.DateField(default=timezone.now,null=True, blank=True)
    updated = models.DateField(default=timezone.now,null=True, blank=True)
    description = models.TextField(blank=True,null=True)
  
    def __str__(self):
        return self.name


class SeatAvailabilty(models.Model):
    bed_type = models.CharField(max_length=250,blank=True,null=True)
    hospital_id = models.IntegerField(blank=True,null=True)
    carecenter_id = models.IntegerField(blank=True,null=True)
    total_beds = models.IntegerField(default=0)
    available_beds = models.IntegerField(default=0)
    

class HospitalSignup(models.Model):
    user_name = models.CharField(max_length=250,blank=True,null=True,unique=True)
    password = models.CharField(max_length=250,blank=True,null=True)
    hospital_id = models.IntegerField()

class CareCenterSignup(models.Model):
    user_name = models.CharField(max_length=250,blank=True,null=True,unique=True)
    password = models.CharField(max_length=250,blank=True,null=True)
    carecenter_id = models.IntegerField()
    