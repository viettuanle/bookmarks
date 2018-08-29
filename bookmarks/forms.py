from django.forms import models
from django import forms

class EmailForm(forms.Form):
    email = forms.CharField()
    message = forms.CharField(label="Message")
    fullname = forms.CharField(label="Your name")