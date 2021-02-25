from django.urls import path, include
from . import views


app_name = "ouvertime_record"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('ouver-time/', views.OuverTimeRecordListView.as_view(), name='ouver-time'),
    path('ouver-time-update/<int:pk>/',
         views.OuverTimeRecordUpdate.as_view(), name='ouver-time-update'),
    path('ouver-time-delete/<int:pk>/',
         views.OuverTimeRecordDelete.as_view(), name='ouver-time-delete'),
    path('ouver-time-create/', views.OuverTimeRecordCreate.as_view(),
         name='ouver-time-create'),
    path('utilizou-hora-extra/<int:pk>/', views.UtilizouHoraExtra.as_view(),
         name='utilizou-hora-extra'),
    path('checked-false/<int:pk>/', views.CheckedFalse.as_view(),
         name='checked-false'),
]
