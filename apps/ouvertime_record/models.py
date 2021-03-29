from django.db import models
from apps.employee.models import Employee
from django.urls import reverse


class OuverTimeRecord(models.Model):
    reason = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.reason

    def get_absolute_url(self):
        return reverse('ouvertime_record:ouver-time')
