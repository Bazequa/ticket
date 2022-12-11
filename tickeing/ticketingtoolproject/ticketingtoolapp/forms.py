from django import forms
from django.contrib.auth.models import User
from .models import ProductModel,ApplicationModel,BookingModel,StationaryModel
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields= ['employee_id','employee_name','priority','your_requirement','Reason']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=ApplicationModel
        fields=['employee_id','employee_name','priority','your_requirement','Reason']

class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingModel
        fields=['employee_id','employee_name','priority','your_requirement','Reason']

class StationaryForm(forms.ModelForm):
    class Meta:
        model=StationaryModel
        fields=['employee_id','employee_name','priority','your_requirement','Reason']



