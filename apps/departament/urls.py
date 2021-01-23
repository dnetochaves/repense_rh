from django.urls import path
from . import views

app_name = "departament"

urlpatterns = [
    path('list_departament/',  views.DepartamentList.as_view(),
         name='list_departament'),
    path('departament-create/',  views.DepartamentCreate.as_view(),
         name='departament-create'),
    path('departament-update/<int:pk>/',  views.DepartamentUpdate.as_view(),
         name='departament-update'),
    path('departament-delete/<int:pk>/',  views.DepartamentDelete.as_view(),
         name='departament-delete'),
]
