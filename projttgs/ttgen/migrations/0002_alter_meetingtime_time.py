# Generated by Django 5.1.1 on 2024-11-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtime',
            name='time',
            field=models.CharField(choices=[('8:50 - 09:50', '8:50 - 09:50'), ('09:50 - 10:45', '09:50 - 10:45'), ('11:00 - 11:55', '11:00 - 11:55'), ('11:55 - 12:50', '11:55 - 12:50'), ('02:00 - 03:00', '02:00 - 03:00'), ('03:00 - 04:00', '03:00 - 04:00'), ('04:00 - 05:00', '04:00 - 05:00')], default='11:30 - 12:30', max_length=50),
        ),
    ]
