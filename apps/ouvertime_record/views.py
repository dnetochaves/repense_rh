from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from . models import OuverTimeRecord
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
import json

# Import for reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


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
        response = json.dumps(
            {'mensagem': 'Requisição execultadass', 'hours': float(employee.sum_overtime)})
        return HttpResponse(response, content_type='application/json')


class CheckedFalse(View):
    def post(self, *args, **kwargs):

        used = OuverTimeRecord.objects.get(id=kwargs['pk'])
        used.used = False
        used.save()

        employee = self.request.user.employee
        response = json.dumps(
            {'mensagem': 'Checked False', 'hours': float(employee.sum_overtime)})
        return HttpResponse(response, content_type='application/json')


# ReportLab
def some_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatorio de Horas ReportLab')

    

    times = OuverTimeRecord.objects.filter(employee=request.user.employee.company.id)

    y = 790
    for time in times:
        p.drawString(10, y, time.reason)
        p.drawString(100, y, time.employee.name)
        p.drawString(200, y, str(time.hours))
        p.drawString(300, y, str(time.used))
        y -= 40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
