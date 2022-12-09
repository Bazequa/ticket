from django import forms
from django.contrib.auth.models import User
from .models import ProductModel,ApplicationModel,BookingModel,StationaryModel
from django.contrib.auth.forms import UserCreationForm

Choices=[(1,'Products'),(2,'Application'),(3,'Booking')]

class SelectType(forms.Form):
    select=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)

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

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class ProductChoiceForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields=['status']

class ApplicationChoiceForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields=['status']

class BookingChoiceForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields=['status']

class StationaryChoiceForm(forms.ModelForm):
    class Meta:
        model = StationaryModel
        fields=['status']