from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from . models import OuverTimeRecord
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
import json
import csv


# Import for reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Import for Xhtm2
from django.template.loader import get_template
from xhtml2pdf import pisa

#import Xlwt
import xlwt


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

    #Metodo desabilitado por mudança de regra
    #def form_valid(self, form):
    #    obj = form.save(commit=False)
    #   obj.employee = self.request.user.employee
    #   obj.save()
    #   return super(OuverTimeRecordUpdate, self).form_valid(form)


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
            {'mensagem': 'Utilizado', 'hours': float(employee.sum_overtime)})
        return HttpResponse(response, content_type='application/json')


class CheckedFalse(View):
    def post(self, *args, **kwargs):

        used = OuverTimeRecord.objects.get(id=kwargs['pk'])
        used.used = False
        used.save()

        employee = self.request.user.employee
        response = json.dumps(
            {'mensagem': 'Não Utilizado', 'hours': float(employee.sum_overtime)})
        return HttpResponse(response, content_type='application/json')


# ReportLab
def some_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatorio de Horas ReportLab')

    times = OuverTimeRecord.objects.filter(
        employee=request.user.employee.company.id)

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

# Xhtml2


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def render_pdf_view(request):
    template_path = 'ouvertime_record/time_report.html'
    cols = OuverTimeRecord.objects.filter(
        employee=request.user.employee.company.id)
    context = {'cols': cols}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'attachment; filename="time-report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class ExportCsv(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        times = OuverTimeRecord.objects.filter(
            employee=request.user.employee.company.id)

        writer = csv.writer(response)
        writer.writerow(['Reason', 'Employee', 'Hours', 'Used'])

        for time in times:
            writer.writerow(
                [time.reason, time.employee.name, time.hours, time.used])

        return response

# Excel


class ExportExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="export_excel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('export_excel')

        row_num = 0

       

        columns = ['Reason', 'Employee', 'Hours', 'Used']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])

        font_style = xlwt.XFStyle()

        times = OuverTimeRecord.objects.filter(
            employee=request.user.employee.company.id)

        row_num = 1
        for time in times:
            ws.write(row_num, 0, time.reason)
            ws.write(row_num, 1, time.employee.name)
            ws.write(row_num, 2, time.hours)
            ws.write(row_num, 3, time.used)
            row_num += 1

        wb.save(response)
        return response
