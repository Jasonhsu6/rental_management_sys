from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *

class EquipmentDetail(DetailView):
    model = Equipment
    template_name = 'equipment/equipment_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EquipmentDetail, self).get_context_data(**kwargs)
        return context


class EquipmentCreate(CreateView):
    model = Equipment
    template_name = 'equipment/forms.html'
    form_class = EquipmentForm

    success_url= '/equipment/'
    def form_valid(self, form):

        return super(EquipmentCreate, self).form_valid(form)


class EquipmentUpdate(UpdateView):
    model = Equipment
    template_name = 'equipment/forms.html'
    fields = [
    'category',
    'vendor',
    'available',
    'day_rate',
    'week_rate',
    'month_rate',
    'retail_price'
    ]


class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = '../'
