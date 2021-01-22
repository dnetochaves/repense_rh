from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Employee
from django.urls import reverse_lazy
from django.contrib.auth.models import User


@login_required
def index(request):
    return HttpResponse('Employee Index')


class ListEmployee(ListView):
    model = Employee

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        queryset = Employee.objects.filter(company=logged_company)
        return queryset


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'departament']


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee:list_employee')

class EmployeeCreate(CreateView):
     model = Employee
     fields = ['name', 'departament']

     def form_valid(self, form):
         obs = form.save(commit=False)
         obs.company = self.request.user.employee.company
         obs.user = User.objects.create(username=obs.name)
         obs.save()
         return super(EmployeeCreate, self).form_valid(form)
