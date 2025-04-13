from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]
    
    contact = models.CharField(max_length=10)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)