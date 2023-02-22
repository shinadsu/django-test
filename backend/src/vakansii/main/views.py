from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm  
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url
from django.http import HttpResponse
from .models import *
from .utils import *
from .forms import *
# Create your views here.


def vakansii_main_page(request):
    jobs = about_job.objects.all()
    form = job_filter_salary(request.GET)
    title = 'Главная страница'
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            jobs = jobs.filter(salary__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            jobs = jobs.filter(salary__lte=form.cleaned_data["max_price"])

    context = {'jobs': jobs, 'form': form, 'title': title, 'menu': menu}
    return render(request, "main/index.html", context=context)


class addjobs(DataMixin, CreateView):
    form_class = add_job
    template_name = 'main/addjob.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление вакансии")
        return dict(list(context.items()) + list(c_def.items()))


class Registermainpage(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'main/registermainpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
    
class Registeruser(DataMixin, CreateView):
    form_class = form_employee
    template_name = 'main/registeruser.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
    
class RegisterForJob(DataMixin, CreateView):
    form_class = form_job
    template_name = 'main/registerforjob.html'
    success_url = reverse_lazy('home')  
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
    
class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    success_url = reverse_lazy('home') 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Аутентификация")
        return dict(list(context.items()) + list(c_def.items()))
    


def show_post(request, post_id):
    post = get_object_or_404(about_job, pk=post_id)
    context = {
        'post': post,
        'title': post.title,
        'menu': menu
    }
    return render(request, "main/full_job.html", context)