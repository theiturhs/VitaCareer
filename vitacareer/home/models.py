from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]
    
    contact = models.CharField(max_length=10)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
class BasicUserDetails(models.Model):
    LOOKING_FOR_CHOICES = [
        ('internship', 'Internship'),
        ('full_time', 'Full Time')
    ]
    FIELD_CHOICES = [
        ('engineering', 'Engineering'),
        ('management', 'Management'),
        ('research', 'Research'),
        ('economins', 'Economics'),
        ('teaching', 'Teaching'),
        ('others', 'Others')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    looking_for = models.CharField(max_length=20, choices=LOOKING_FOR_CHOICES)
    field = models.CharField(max_length=20, choices=FIELD_CHOICES)
    bio = models.CharField(max_length=200)
    organization = models.CharField(max_length=20)
    job_role = models.CharField(max_length=20)
    experience = models.IntegerField()