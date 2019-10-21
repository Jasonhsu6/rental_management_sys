from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *

@login_required
def index(request):
    return render(request, 'RentalNavigate.html')

class RentalDetail(LoginRequiredMixin, DetailView):
    model = Rental
    template_name = 'rental/rental_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RentalDetail, self).get_context_data(**kwargs)
        print(context)
        return context

class RentalCreate(PermissionRequiredMixin ,CreateView):
    permission_required = 'rental.add_job'
    model = Rental
    template_name = 'rental/forms.html'
    form_class = RentalForm

    success_url= '/rental/rental'
    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form.instance.equipment)

        return super(RentalCreate, self).form_valid(form)


class RentalUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'rental.change_rental'
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


class RentalDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'rental.delete_rental'
    model = Rental
    success_url = '/rental/rental'

def rental_search(request):
    query = request.GET.get('search')

    if query:
        # return Rental.objects.filter(job__project_manager__username__contains=query)
        return Rental.objects.filter(equipment__category__name__contains=query)

    else:
        return Rental.objects.all()

class RentalList(LoginRequiredMixin, ListView):
    template_name='rental/rental_list.html'
    context_object_name='rental_list'
    model= Rental
    def get_queryset(self):
        return rental_search(self.request)
    # queryset = rental_search


class JobDetail(LoginRequiredMixin,DetailView):
    model = Job
    template_name = 'job/job_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetail, self).get_context_data(**kwargs)
        return context


class JobCreate(PermissionRequiredMixin,CreateView):
    model = Job
    template_name = 'rental/forms.html'
    permission_required = 'rental.add_job'
    form_class = JobForm

    success_url= '/rental/job'
    def form_valid(self, form):

        form.instance.project_manager = self.request.user
        print(form.instance)
        return super(JobCreate, self).form_valid(form)


class JobUpdate(PermissionRequiredMixin,UpdateView):
    model = Job
    template_name = 'rental/forms.html'
    permission_required = 'rental.change_job'

    fields = [
        'name',
        'site',
        'active',
        'supervisor',
        'PO_num',
    ]
    success_url = '/rental/job'


class JobDelete(PermissionRequiredMixin,DeleteView):
    model = Job
    permission_required = 'rental.delete_job'

    success_url = '/rental/job'
    template_name = 'rental/rental_confirm_delete.html'
