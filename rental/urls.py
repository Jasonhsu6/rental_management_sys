from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView

from rental import views
from . views import *
from .models import *

app_name='rental'
urlpatterns = [
    path('', views.index),

    path('rental/', ListView.as_view(
        queryset=Rental.objects.all(),
        template_name='rental/rental_list.html',
        context_object_name='rental_list'
    ), name='rental_list'),
    path('rental/<int:pk>/', RentalDetail.as_view(), name='rental_detail'),
    path('rental/create/', RentalCreate.as_view(), name='rental_create'),
    path('rental/<int:pk>/edit/', RentalUpdate.as_view(), name='rental_update'),
    path('rental/<int:pk>/delete/', RentalDelete.as_view(), name='rental_confirm_delete'),

    path('job/', ListView.as_view(
        queryset=Job.objects.all(),
        template_name='job/job_list.html',
        context_object_name='job_list'
    ), name='job_list'),
    path('job/<int:pk>/', JobDetail.as_view(), name='job_detail'),
    path('job/create/', JobCreate.as_view(), name='job_create'),
    path('job/<int:pk>/edit/', JobUpdate.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', JobDelete.as_view(), name='job_confirm_delete'),
]
