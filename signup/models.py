from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class User(AbstractUser):
#     is_moderator = models.BooleanField(default=False)
#     is_employee = models.BooleanField(default=False)
#
# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, primary_key=True)
#
# class Moderator(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, primary_key=True)