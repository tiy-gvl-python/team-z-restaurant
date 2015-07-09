from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class FoodItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)


class Address(models.Model):
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)
    plus_4 = models.CharField(max_length=4)


class Customer(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.ForeignKey(Address)
    telephone = models.IntegerField(max_length=10)
    user = models.OneToOneField(User)


class Owner(models.Model):
    name = models.CharField(max_length=40)
    telephone = models.IntegerField(max_length=10)
    user = models.OneToOneField(User)


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner)
    address = models.OneToOneField(Address)
    telephone = models.IntegerField(max_length=10)


class Order(models.Model):
    food_item = models.ManyToManyField(FoodItem)
    restaurant = models.ForeignKey(Restaurant)
    instructions = models.CharField(max_length=100, blank=True)

