# Generated by Django 4.1.7 on 2023-02-21 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_about_job_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_job',
            name='is_published',
        ),
    ]
