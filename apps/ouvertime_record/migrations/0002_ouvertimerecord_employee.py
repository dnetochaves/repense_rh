# Generated by Django 3.1.5 on 2021-01-16 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210116_0815'),
        ('ouvertime_record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ouvertimerecord',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='employee.employee'),
            preserve_default=False,
        ),
    ]
