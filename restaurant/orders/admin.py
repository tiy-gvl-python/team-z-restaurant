from django.contrib import admin

# Register your models here.
from orders.models import FoodItem, Customer, Address, Restaurant, Order, Owner

admin.site.register(FoodItem)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Owner)