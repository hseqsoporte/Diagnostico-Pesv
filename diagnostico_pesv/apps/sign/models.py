from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    licensia_sst = models.CharField(max_length=250, blank=False, null=True, default=None)
    cedula = models.CharField(max_length=10, blank=True, null=None, unique=True)