from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Departament
from django.http import HttpResponse
from django.urls import reverse_lazy


class DepartamentList(ListView):
    model = Departament

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        queryset = Departament.objects.filter(company=logged_company)
        return queryset


class DepartamentCreate(CreateView):
    model = Departament
    fields = ['name']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user.employee.company
        obj.save()
        return super(DepartamentCreate, self).form_valid(form)


class DepartamentUpdate(UpdateView):
    model = Departament
    fields = ['name']


class DepartamentDelete(DeleteView):
    model = Departament
    success_url = reverse_lazy('departament:list_departament')
