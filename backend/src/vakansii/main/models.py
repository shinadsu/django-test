from django.db import models
from django.urls import reverse

# Create your models here.

class about_job(models.Model):
    title = models.CharField(max_length=255, verbose_name="Вакансия", )
    photo = models.ImageField(null=True, upload_to="photos/%Y/%m/%d/")
    content = models.TextField(blank=True, verbose_name="Описание", )
    salary = models.IntegerField(default=True, verbose_name="Зарплата")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})
    
    


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name
    


class employer(models.Model):
    username = models.CharField(max_length=255, verbose_name="username", )
    passwod = models.CharField(max_length=255, verbose_name="password", )
    Name = models.CharField(max_length=255, verbose_name="Имя", )
    Surname = models.CharField(max_length=255, verbose_name="Фамилия", )
    patronymic = models.CharField(max_length=255, verbose_name="Отчество", )
    number_of_workers = models.IntegerField(null=False, verbose_name="Количество сотрудников", )
    Placement = models.CharField(max_length=255, verbose_name="Место нахождение (указать город)", )
    company_name = models.CharField( max_length=255, verbose_name="Название компании", )
    About = models.CharField(max_length=255, verbose_name="О компании", )
    
    

class Employee(models.Model):
    username = models.CharField(max_length=255, verbose_name="username", )
    passwod = models.CharField(max_length=255, verbose_name="password", )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    
