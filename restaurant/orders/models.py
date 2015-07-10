from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class MenuItem(models.Model):
    APPETIZER = 'App'
    ENTREE = 'Ent'
    DESERT = 'Des'
    DRINK = 'Dri'
    MENU_CHOICES = (
        (APPETIZER, 'Appetizer'),
        (ENTREE, 'Entree'),
        (DESERT, 'Desert'),
        (DRINK, 'Drink')
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu_parts = models.CharField(max_length=20, choices=MENU_CHOICES, default=APPETIZER, blank=True)


class Address(models.Model):
    STATE_CHOICES = (('AL','Alabama'),
                    ('AK','Alaska'),
                    ('AZ','Arizona'),
                    ('AR','Arkansas'),
                    ('CA','California'),
                    ('CO','Colorado'),
                    ('CT','Connecticut'),
                    ('DE','Delaware'),
                    ('DC','District of Columbia'),
                    ('FL','Florida'),
                    ('GA','Georgia'),
                    ('HI','Hawaii'),
                    ('ID','Idaho'),
                    ('IL','Illinois'),
                    ('IN','Indiana'),
                    ('IA','Iowa'),
                    ('KS','Kansas'),
                    ('KY','Kentucky'),
                    ('LA','Louisiana'),
                    ('ME','Maine'),
                    ('MD','Maryland'),
                    ('MA','Massachusetts'),
                    ('MI','Michigan'),
                    ('MN','Minnesota'),
                    ('MS','Mississippi'),
                    ('MO','Missouri'),
                    ('MT','Montana'),
                    ('NE','Nebraska'),
                    ('NV','Nevada'),
                    ('NH','New Hampshire'),
                    ('NJ','New Jersey'),
                    ('NM','New Mexico'),
                    ('NY','New York'),
                    ('NC','North Carolina'),
                    ('ND','North Dakota'),
                    ('OH','Ohio'),
                    ('OK','Oklahoma'),
                    ('OR','Oregon'),
                    ('PA','Pennsylvania'),
                    ('RI','Rhode Island'),
                    ('SC','South Carolina'),
                    ('SD','South Dakota'),
                    ('TN','Tennessee'),
                    ('TX','Texas'),
                    ('UT','Utah'),
                    ('VT','Vermont'),
                    ('VA','Virginia'),
                    ('WA','Washington'),
                    ('WV','West Virginia'),
                    ('WI','Wisconsin'),
                    ('WY','Wyoming'))
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, default='AL')
    zipcode = models.CharField(max_length=5)
    plus_4 = models.CharField(max_length=4, blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.ForeignKey(Address)
    telephone = models.CharField(max_length=10)
    user = models.OneToOneField(User)


class Owner(models.Model):
    name = models.CharField(max_length=40)
    telephone = models.CharField(max_length=10)
    user = models.OneToOneField(User)


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner)
    address = models.OneToOneField(Address)
    telephone = models.CharField(max_length=10)


class Order(models.Model):
    menu_item = models.ManyToManyField(MenuItem)
    restaurant = models.ForeignKey(Restaurant)
    instructions = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer)
