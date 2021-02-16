from django.db import models
from django.contrib.auth.models import User
from apps.departament.models import Departament
from apps.company.models import Company
from django.urls import reverse
from django.db.models import Avg, Count, Min, Sum


class Employee(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departament = models.ManyToManyField(Departament)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    cpf = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='photo')

    @property
    def sum_overtime(self):
        total = self.ouvertimerecord_set.filter(used=False).aggregate(Sum('hours'))[
            'hours__sum']
        return total or 0

    def get_absolute_url(self):
        return reverse('employee:list_employee')

    def __str__(self):
        return self.name
