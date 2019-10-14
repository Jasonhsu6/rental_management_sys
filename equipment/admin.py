from django.contrib import admin

# Register your models here.
from .models import Equipment, Vendor, Category

admin.site.register(Equipment)
admin.site.register(Vendor)
admin.site.register(Category)
