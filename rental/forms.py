from django.forms import ModelForm, DateTimeInput
from .models import Rental, Job
from django.contrib.admin import widgets


class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = [
            'job',
            'equipment',
            'received_date',
            'return_date',
            'buy_or_rent',
            'entered_via',
            'comments',
        ]


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            'name',
            'site',
            'active',
            'supervisor',
            'PO_num',
        ]
