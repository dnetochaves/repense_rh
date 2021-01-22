from django.urls import path, include
from . import views

app_name = "employee"

urlpatterns = [
    path('index/',  views.index, name='index'),
    path('list_employee/',  views.ListEmployee.as_view(), name='list_employee'),
    path('employee_update/<int:pk>/',  views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee_delete/<int:pk>/',  views.EmployeeDelete.as_view(), name='employee_delete'),
    path('employee_create/',  views.EmployeeCreate.as_view(), name='employee_create'),
]
