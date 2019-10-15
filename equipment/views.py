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

    success_url= '/equipment/equipment'
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
    # success_url= '/equipment/equipment'




class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = '../'

class VendorDetail(DetailView):
    model = Vendor
    template_name = 'vendor/vendor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VendorDetail, self).get_context_data(**kwargs)
        return context

class VendorCreate(CreateView):
    model = Vendor
    template_name = 'equipment/forms.html'
    form_class = VendorForm

    success_url= '/equipment/vendor'
    def form_valid(self, form):

        return super(VendorCreate, self).form_valid(form)

class VendorUpdate(UpdateView):
    model = Vendor
    template_name = 'equipment/forms.html'
    fields = [
    'name',
    'address',
    'email',
    'phone',
    ]
    # success_url= '/equipment/vendor'


class VendorDelete(DeleteView):
    model = Vendor
    success_url = '../'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        return context

class CategoryCreate(CreateView):
    model = Category
    template_name = 'equipment/forms.html'
    form_class = CategoryForm

    success_url= '/equipment/category'
    def form_valid(self, form):

        return super(CategoryCreate, self).form_valid(form)

class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'equipment/forms.html'
    fields = [
    'name',
    ]
    # success_url= '/equipment/category'


class CategoryDelete(DeleteView):
    model = Category
    success_url = '../'
