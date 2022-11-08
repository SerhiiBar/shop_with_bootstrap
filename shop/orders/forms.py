from django import forms
from .models import Order
from cart.cart import Cart


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city']

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
