from django import forms
from orders.models import Customer, Address, Owner, Restaurant


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ["user", "address"]


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = []


class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        exclude = ["user"]


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        exclude = ["address"]