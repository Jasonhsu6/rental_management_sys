from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_moderator = models.BooleanField(default=false)
    is_employee = models.BooleanField(default=false)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, primary_key=True)

class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, primary_key=True)
>>>>>>> 33c1eb452f33419e85fbd20e0b4ba4c94d27c6b2
