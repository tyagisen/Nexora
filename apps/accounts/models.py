from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.common.models import BaseModel
from .managers import UserManager

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #This is a extra field that asks in CLI

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.email
    

    
