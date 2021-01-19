from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Company
from apps.employee.models import Employee
from django.http import HttpResponse


def index(request):
    return HttpResponse('Index')


def company(request):
    companys = Employee.objects.filter(pk=request.user.id)
    return render(request, 'company/company.html', {'companys': companys})


class CompanyCreate(CreateView):
    model = Company
    fields = ['name']

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()
        return HttpResponse('Ok')


class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name']
