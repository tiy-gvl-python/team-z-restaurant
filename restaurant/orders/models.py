from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Food_Item(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)


class Order(models.Model):
    food_item = models.ManyToManyField(Food_Item)
    restaurant = models.ForeignKey(Restaurant)
    instructions = models.CharField(max_length=100, blank=True)

class Address(models.Model):
    line_1 = models.CharField(max_length=30)
    line_2 = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    plus_4 = models.CharField(max_length=4)


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField() #  customize the arguments
    address = models.ForeignKey(Address)
    telephone = models.IntegerField(max_length=10)
    user = models.OneToOneField(User)

class Owner(models.Model):
    name = models.CharField(max_length=30)
    telephone = models.IntegerField(max_length=10)
    user = models.OneToOneField(User)

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner)
    address = models.OneToOneField(Address)
    telephone = models.IntegerField(max_length=10)




