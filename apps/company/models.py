from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, help_text="Company Namess")

    def __str__(self):
        return self.name
