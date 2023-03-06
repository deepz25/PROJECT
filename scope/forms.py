from django import forms
from .models import *


class Login_Form(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username','class':"form-control bg-light border-0 px-4"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password','class':"form-control bg-light border-0 px-4"}))

class DateInput(forms.DateInput):
    input_type = 'date'





