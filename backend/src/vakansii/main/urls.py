from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', vakansii_main_page, name='home'),
    path('addjobtosite/', addjobs.as_view(), name='addjob'),
    path('registermainpage/', Registermainpage.as_view(), name='registermainpage'),
    path('register/', Registeruser.as_view(), name='registeruser'),
    path('registerjob/', RegisterForJob.as_view(), name='registerforjob'),
    path('login/', LoginUser.as_view(), name='login'), 
    path('post/<int:post_id>/', show_post, name='post'),
    # я осознанно делаю так {post_id}, зная, что в реальных проектах используется slug 
    # так как лучше ранжируется 
]