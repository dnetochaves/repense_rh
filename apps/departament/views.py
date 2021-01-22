from django.shortcuts import render
from django.views.generic.list import ListView
from . models import Departament
from django.http import HttpResponse


class DepartamentList(ListView):
    model = Departament
    

def index(request):
    return HttpResponse('Teste')
    