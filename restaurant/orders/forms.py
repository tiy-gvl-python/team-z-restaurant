from django import forms
from django.contrib.auth.forms import UserCreationForm
from orders.models import Customer, Address


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ["user", "address"]


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = []
