
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomDateInput(forms.DateInput):
    input_formats = 'date'

class CreatengoForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class CreateDoctorForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
# forms.py

class MedicineForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = '__all__'
