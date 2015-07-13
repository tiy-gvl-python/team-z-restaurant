from django.contrib import admin

# Register your models here.
from django_cryptocoin.models import ExchangeRate, CryptoOrder
from orders.models import MenuItem, Customer, Address, Restaurant, Order, Owner, CartOption

admin.site.register(MenuItem)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Owner)
admin.site.register(CartOption)
admin.site.register(ExchangeRate)
admin.site.register(CryptoOrder)