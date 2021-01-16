# Generated by Django 3.1.5 on 2021-01-16 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210116_0820'),
        ('documents', '0002_documents_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='employee.employee'),
            preserve_default=False,
        ),
    ]