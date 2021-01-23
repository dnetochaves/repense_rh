from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Documents
from apps.employee.models import Employee


class DocumentList(ListView):
    model = Documents

    def get_queryset(self):
        owner = self.request.user.employee
        queryset = Documents.objects.filter(owner=owner)
        return queryset


class DocumentCreate(CreateView):
    model = Documents
    fields = ['description', 'doc']

    def form_valid(self, form):
        obj = form.save(commit=False)
        employee_id = Employee.objects.get(user=self.request.user)
        obj.owner = employee_id
        obj.save()
        return super(DocumentCreate, self).form_valid(form)
