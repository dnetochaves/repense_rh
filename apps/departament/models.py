from django.db import models
from apps.company.models import Company
from django.urls import reverse


class Departament(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('departament:list_departament')

    def __str__(self):
        return self.name
