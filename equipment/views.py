from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import *

def index(request):
    return render(request, 'EquipmentNavigate.html')

class EquipmentDetail(LoginRequiredMixin, DetailView):
    permission_denied_message = 'You must log in first'
    model = Equipment
    template_name = 'equipment/equipment_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EquipmentDetail, self).get_context_data(**kwargs)
        return context


class EquipmentCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'equipment.add_equipment'
    permission_denied_message = "You are not allowed to create a new equipment"
    model = Equipment
    template_name = 'equipment/forms.html'
    form_class = EquipmentForm

    success_url= '/equipment/equipment'
    def form_valid(self, form):

        return super(EquipmentCreate, self).form_valid(form)


class EquipmentUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'equipment.change_equipment'
    permission_denied_message = "You are not allowed to update a new equipment"
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
    help_text= "Equipment"

    # success_url= '/equipment/equipment'




class EquipmentDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'equipment.delete_equipment'
    permission_denied_message = 'You cannot delete equipment'
    model = Equipment
    success_url = '../'

class VendorDetail(LoginRequiredMixin, DetailView):
    permission_denied_message = 'You must login first'
    model = Vendor
    template_name = 'vendor/vendor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VendorDetail, self).get_context_data(**kwargs)
        return context

class VendorCreate(PermissionRequiredMixin, CreateView):
    permission_denied_message = 'You cannot create a new vendor'
    permission_required = 'equipment.add_vendor'
    model = Vendor
    template_name = 'equipment/forms.html'
    form_class = VendorForm

    success_url= '/equipment/vendor'
    def form_valid(self, form):

        return super(VendorCreate, self).form_valid(form)

class VendorUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'equipment.change_vendor'
    permission_denied_message = 'You cannot update vendor'
    model = Vendor
    template_name = 'equipment/forms.html'
    fields = [
    'name',
    'address',
    'email',
    'phone',
    ]
    # success_url= '/equipment/vendor'


class VendorDelete(PermissionRequiredMixin, DeleteView):
    permission_denied_message = 'You cannot delete vendor information'
    permission_required = 'equipment.delete_vendor'
    model = Vendor
    success_url = '../'


class CategoryDetail(LoginRequiredMixin, DetailView):
    permission_denied_message = 'You must login first'
    model = Category
    template_name = 'category/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        return context

class CategoryCreate(PermissionRequiredMixin, CreateView):
    permission_denied_message = 'You are not allowed to create a category'
    permission_required = 'equipment.add_category'
    model = Category
    template_name = 'equipment/forms.html'
    form_class = CategoryForm

    success_url= '/equipment/category'
    def form_valid(self, form):

        return super(CategoryCreate, self).form_valid(form)

class CategoryUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'equipment.change_category'
    permission_denied_message = 'You cannot update a category'
    model = Category
    template_name = 'equipment/forms.html'
    fields = [
    'name',
    ]
    # success_url= '/equipment/category'


class CategoryDelete(PermissionRequiredMixin, DeleteView):
    permission_denied_message = 'You are not allowed to delete a category'
    permission_required = 'equipment.delete_category'
    model = Category
    success_url = '../'
