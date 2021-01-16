from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    employee = request.user
    return render(request, 'core/index.html', {'employee': employee})

