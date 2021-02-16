from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from . models import OuverTimeRecord
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
import json


def index(request):
    return HttpResponse('ok')


class OuverTimeRecordListView(ListView):

    model = OuverTimeRecord
    # paginate_by = 100  # if pagination is desired

    def get_queryset(self):
        logged_company = self.request.user.employee.company.id
        queryset = OuverTimeRecord.objects.filter(employee=logged_company)
        return queryset


class OuverTimeRecordUpdate(UpdateView):
    model = OuverTimeRecord
    fields = ['reason', 'hours']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.employee = self.request.user.employee
        obj.save()
        return super(OuverTimeRecordUpdate, self).form_valid(form)


class OuverTimeRecordDelete(DeleteView):
    model = OuverTimeRecord
    success_url = reverse_lazy('ouvertime_record:ouver-time')


class OuverTimeRecordCreate(CreateView):
    model = OuverTimeRecord
    fields = ['reason', 'hours']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.employee = self.request.user.employee
        obj.save()
        return super(OuverTimeRecordCreate, self).form_valid(form)


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        used = OuverTimeRecord.objects.get(id=kwargs['pk'])
        used.used = True
        used.save()

        employee = self.request.user.employee
        print(f'################################{employee.sum_overtime}')
        response = json.dumps(
            {'mensagem': 'Requisição execultadass', 'hours': float(employee.sum_overtime) })
        return HttpResponse(response, content_type='application/json')
