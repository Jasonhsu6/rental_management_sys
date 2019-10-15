from django.db import models
from equipment.models import Equipment
from django.contrib.auth.models import User
# Create your models here.

class Rental(models.Model):
    job = models.ForeignKey('Job', on_delete = models.SET_NULL, null=True)
    equipment = models.OneToOneField(Equipment, on_delete = models.SET_NULL, null=True)
    # equipment = models.ForeignKey(Equipment, on_delete = models.SET_NULL, null=True)

    entered_date = models.DateTimeField(auto_now = True)
    received_date = models.DateTimeField(null = True, blank = True)
    return_date = models.DateTimeField(null=True, blank=True)
    buy_or_rent = models.CharField(max_length = 4, choices = [('Buy', 'Buy'), ('Rent', 'Rent')])
    comments = models.TextField(max_length = 140, null=True)
    entered_via = models.CharField(max_length = 2,
                                   choices = [('O', 'Order'),('I','Invoice'),('R','Rental Slip')])


class Job(models.Model):
    name = models.CharField(max_length = 20, unique=True)
    project_manager = models.ForeignKey(User, on_delete = models.SET_NULL, null=True,
                                        related_name='project_manager')
    site = models.CharField(max_length = 30)
    active = models.BooleanField(default = True)
    supervisor = models.OneToOneField(User, on_delete = models.SET_NULL, null=True,
                                   related_name='supervisor')
    PO_num = models.CharField(max_length = 10)
    def __str__(self):
        return self.name
