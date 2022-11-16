from django import forms
from django.shortcuts import render

from .models import Order
from mainapp.models import Category


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'city']

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
