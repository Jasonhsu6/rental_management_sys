from django.forms import ModelForm
from .models import Equipment, Category, Vendor

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = [
        'category',
        'vendor',
        'name',
        'serial_number',
        'available',
        'day_rate',
        'week_rate',
        'month_rate',
        'retail_price'
        ]
        help_text= "Equipment"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields= [
        'name',
        'address',
        'email',
        'phone'
        ]
