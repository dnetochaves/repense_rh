from django.db import models
from apps.employee.models import Employee
from django.urls import reverse

class Documents(models.Model):
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(Employee, on_delete=models.PROTECT)
    doc = models.FileField(upload_to='documents')

    def get_absolute_url(self):
        return reverse('documents:document-list')

    def __str__(self):
        return self.description
    
