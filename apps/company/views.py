from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Company
from apps.employee.models import Employee
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return HttpResponse('Index')


def company(request):
    user_employee = Employee.objects.get(pk=request.user.employee.id)
    companys = Employee.objects.filter(company=user_employee.company_id)
    return render(request, 'company/company.html', {'companys': companys, 'user_employee': user_employee})
    

class CompanyCreate(CreateView):
    model = Company
    fields = ['name']

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()
        return HttpResponse('Ok')


class CompanyUpdate(SuccessMessageMixin, UpdateView):
    model = Company
    fields = ['name']
    success_message = "Dados atualizados com sucesso!!"
    
    

   
