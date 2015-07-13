from django import forms
from django_cryptocoin.settings import CRYPTO_COINS
from orders.models import Customer, Address, Owner, Restaurant, Order


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ["user", "address"]


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ["zip4"]


class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        exclude = ["user"]


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        exclude = ["address"]


class OrderPaymentForm(forms.ModelForm):
    currency = forms.CharField(max_length=50, widget=forms.Select(choices=CRYPTO_COINS.items()))

    class Meta:
        model = Order
        exclude = ['menu_item', 'crypto_order', 'status', 'customer']