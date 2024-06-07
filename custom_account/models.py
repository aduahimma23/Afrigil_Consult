from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=15, blank=False, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=False)
    confirm_password = models.CharField(max_length=100, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        super().save(*args, **kwargs)
