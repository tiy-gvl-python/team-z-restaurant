# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
from django.contrib.auth.models import User

from django.db import models, migrations
from orders.models import Address, Customer


def data_migrate(x, y):
    with open('../data/customer.csv') as file:
        file_lines = csv.DictReader(file)
        for line in file_lines:
            user = User(username=line["name"])
            user.set_password("customer")
            user.save()
            address = Address.objects.create(line_1=line["line_1"],line_2=line["line_2"], city=line["city"],
                                             state=line["state"], zipcode=line["zip5"])
            Customer.objects.create(name=line["name"], telephone=line["telephone"],
                                    address=address, user=user, email=line["email"])


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20150712_1949'),
    ]

    operations = [
        migrations.RunPython(data_migrate),
    ]
