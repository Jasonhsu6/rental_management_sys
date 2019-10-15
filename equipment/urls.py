from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView
from . views import EquipmentDelete,EquipmentDetail,EquipmentUpdate, EquipmentCreate
from .models import Equipment

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
    path('equipment/<int:pk>/delete',EquipmentDelete.as_view(), name='equipment_confirm_delete')


]
