# Generated by Django 4.1.7 on 2023-02-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_employee_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_birth',
        ),
    ]