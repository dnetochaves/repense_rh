from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Company
from django.http import HttpResponse

def index(request):
    return HttpResponse('Index')


class CompanyCreate(CreateView):
    model = Company
    fields = ['name']

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()
        return HttpResponse('Ok')
