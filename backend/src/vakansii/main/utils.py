from django.db.models import Count

from .models import *

menu = [{'title': "Вакансии", 'url_name': 'home'},
        {'title': "Добавить вакансию", 'url_name': 'addjob'},]

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu

        return context