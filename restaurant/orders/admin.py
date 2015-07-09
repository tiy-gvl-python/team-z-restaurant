from django.contrib import admin

# Register your models here.
from orders.models import FoodItem, Customer, Address, Restaurant, Order, Owner

admin.register(FoodItem)
admin.register(Customer)
admin.register(Address)
admin.register(Restaurant)
admin.register(Order)
admin.register(Owner)