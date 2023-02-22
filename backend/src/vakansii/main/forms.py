from django import forms
from .models import *

class job_filter_salary(forms.Form):
    min_price = forms.IntegerField(label='от', required=False)
    max_price = forms.IntegerField(label='до', required=False)


class add_job(forms.ModelForm):

    class Meta:
        model = about_job
        fields = '__all__'
        widgets = {
            'title': forms.TimeInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


class form_employee(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
        
        

class form_job(forms.ModelForm):
    
    class Meta:
        model = employer
        fields = '__all__'
        
        
class login_FORM(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['email', 'phone_number']
      