# Generated by Django 3.1.5 on 2021-01-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_employee_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cpf',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]