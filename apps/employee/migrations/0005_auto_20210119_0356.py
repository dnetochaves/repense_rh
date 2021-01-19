# Generated by Django 3.1.5 on 2021-01-19 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20210119_0347'),
        ('employee', '0004_auto_20210119_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company'),
        ),
    ]
