from django.db import models

# Create your models here.



class Equipment(models.Model):
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)
    vendor = models.ForeignKey('Vendor', on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length = 50)
    serial_number = models.CharField(max_length = 6, unique=True)
    available = models.BooleanField(default = True)
    day_rate = models.FloatField(default = 0)
    week_rate = models.FloatField(default = 0)
    month_rate = models.FloatField(default = 0)
    retail_price = models.FloatField(default = 0)
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length = 20, unique=True)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length = 11)
    def __str__(self):
        return self.name