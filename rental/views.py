from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *

class RentalDetail(DetailView):
    model = Rental
    template_name = 'rental/rental_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RentalDetail, self).get_context_data(**kwargs)
        return context


class RentalCreate(CreateView):
    model = Rental
    template_name = 'rental/forms.html'
    form_class = RentalForm

    success_url= '/rental/rental'
    def form_valid(self, form):

        return super(RentalCreate, self).form_valid(form)


class RentalUpdate(UpdateView):
    model = Rental
    template_name = 'rental/forms.html'
    fields = [
        'job',
        'equipment',
        'received_date',
        'return_date',
        'buy_or_rent',
        'entered_via',
        'comments',
    ]
    success_url = '/rental/rental'


class RentalDelete(DeleteView):
    model = Rental
    success_url = '/rental/rental'




class JobDetail(DetailView):
    model = Job
    template_name = 'job/job_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetail, self).get_context_data(**kwargs)
        return context


class JobCreate(CreateView):
    model = Job
    template_name = 'rental/forms.html'
    form_class = JobForm

    success_url= '/rental/job'
    def form_valid(self, form):

        return super(JobCreate, self).form_valid(form)


class JobUpdate(UpdateView):
    model = Job
    template_name = 'rental/forms.html'
    fields = [
        'name',
        'site',
        'active',
        'supervisor',
        'PO_num',
    ]
    success_url = '/rental/job'


class JobDelete(DeleteView):
    model = Job
    success_url = '/rental/job'
