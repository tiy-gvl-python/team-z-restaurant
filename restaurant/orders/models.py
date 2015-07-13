from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django_cryptocoin.models import CryptoOrder
from django_cryptocoin.signals import after_pay_confirmation

# Constants
ORDER_STATES = (('In Cart', 'In Cart'),
                ('Submitted', 'Submitted'),
                ('Payment Received', 'Payment Received'),
                ('Being Cooked', 'Being Cooked'),
                ('Out for Delivery', 'Out for Delivery'),
                ('Delivered', 'Delivered'))

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

MENU_CHOICES = (
                ('Appetizer', 'Appetizer'),
                ('Entree', 'Entree'),
                ('Dessert', 'Dessert'),
                ('Drink', 'Drink')
    )

# Models

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu_parts = models.CharField(max_length=20, choices=MENU_CHOICES, default='App', blank=True)

    def __str__(self):
        return self.title


class Address(models.Model):
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=5)
    plus_4 = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return "{}\n{}, {} {}".format(self.line_1, self.city, self.city, self.state, self.zipcode)


class Customer(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.ForeignKey(Address)
    telephone = models.CharField(max_length=10)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=40)
    telephone = models.CharField(max_length=10)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner)
    address = models.OneToOneField(Address)
    telephone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Order(models.Model):
    menu_item = models.ManyToManyField(MenuItem, through="CartOption")
    restaurant = models.ForeignKey(Restaurant)
    instructions = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer)
    status = models.CharField(choices=ORDER_STATES, max_length=50, default='In Cart')
    crypto_order = models.OneToOneField(CryptoOrder, related_name='order', null=True)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.customer.name, self.status)

    @property
    def total_cost(self):
        return sum([cart_option.price for cart_option in self.cartoption_set.all()])


@receiver(after_pay_confirmation)
def submit_order(sender, **kwargs):
    print(sender.order)
    sender.order.status = 'Payment Received'
    sender.order.save()


class CartOption(models.Model):
    menu_item = models.ForeignKey(MenuItem)
    order = models.ForeignKey(Order)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Order: {}; {} {}".format(self.order.id, self.quantity, self.menu_item.title)

    @property
    def price(self):
        return self.menu_item.price * self.quantity