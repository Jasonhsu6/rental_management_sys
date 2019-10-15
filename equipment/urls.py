from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView
from . views import *
from .models import Equipment, Vendor, Category

app_name= 'equipment'
urlpatterns = [
    path('equipment/', ListView.as_view(
    queryset = Equipment.objects.all(),
    template_name='equipment/equipment_list.html',
    context_object_name = 'total_equipment_list'
    ), name='equipment_list'),
    path('equipment/<int:pk>',EquipmentDetail.as_view(), name='equipment_detail'),
    path('equipment/create', EquipmentCreate.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/edit',EquipmentUpdate.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete',EquipmentDelete.as_view(), name='equipment_confirm_delete'),

    path('vendor/', ListView.as_view(
    queryset = Vendor.objects.all(),
    template_name='vendor/vendor_list.html',
    context_object_name = 'total_vendor_list'
    ), name='vendor_list'),
    path('vendor/<int:pk>',VendorDetail.as_view(), name='vendor_detail'),
    path('vendor/create', VendorCreate.as_view(), name='vendor_create'),
    path('vendor/<int:pk>/edit',VendorUpdate.as_view(), name='vendor_update'),
    path('vendor/<int:pk>/delete',VendorDelete.as_view(), name='vendor_confirm_delete'),

    path('category/', ListView.as_view(
    queryset = Category.objects.all(),
    template_name='category/category_list.html',
    context_object_name = 'total_category_list'
    ), name='category_list'),
    path('category/<int:pk>',CategoryDetail.as_view(), name='category_detail'),
path('category/create', CategoryCreate.as_view(), name='category_create'),
path('category/<int:pk>/edit',CategoryUpdate.as_view(), name='category_update'),
path('category/<int:pk>/delete',CategoryDelete.as_view(), name='category_confirm_delete'),



]
