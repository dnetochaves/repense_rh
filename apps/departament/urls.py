from django.urls import path
from . import views

app_name = "departament"

urlpatterns = [
    path('list_departament/',  views.DepartamentList.as_view(),
         name='list_departament'),
]
