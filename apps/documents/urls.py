from django.urls import path
from . import views


app_name = "documents"

urlpatterns = [
    path('document-create/',  views.DocumentCreate.as_view(),
         name='document-create'),
    path('document-list/',  views.DocumentList.as_view(), name='document-list'),
]
