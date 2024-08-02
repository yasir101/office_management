from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
      ('admin', 'Admin'),
      ('hr', 'HR'),
      ('employee', 'Employee'),
      ('office_boy', 'Office Boy'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='employee')