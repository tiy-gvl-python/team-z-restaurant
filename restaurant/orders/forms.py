from django import forms
from django.contrib.auth.forms import UserCreationForm
from orders.models import Customer, Address


class CustomerCreationForm(UserCreationForm):
    name = forms.CharField(max_length=40)
    address_line_1 = forms.CharField(max_length=100)
    address_line_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=20)
    state = forms.CharField(max_length=2)
    zip5 = forms.CharField(max_length=5)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=10)


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ["user", "address"]


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = []


