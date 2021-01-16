from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Company


@login_required
def index(request):
    return HttpResponse('Employee Index')


