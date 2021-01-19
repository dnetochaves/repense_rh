from django.urls import path, include
from . import views 


app_name = "company"

urlpatterns = [
    path('index/',  views.index, name='index'),
    path('company_create/',  views.CompanyCreate.as_view(), name='company_create'),
    path('company_update/<int:pk>/',  views.CompanyUpdate.as_view(), name='company_update'),
    path('company/',  views.company, name='company'),
]
