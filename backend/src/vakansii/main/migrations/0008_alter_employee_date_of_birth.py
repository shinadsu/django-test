# Generated by Django 4.1.7 on 2023-02-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_company_employer_alter_about_job_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=True),
        ),
    ]
