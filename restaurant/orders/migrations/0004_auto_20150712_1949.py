# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations
from orders.models import Address, Restaurant, Owner


def data_migrate(x, y):
    with open('../data/restaurant.csv') as file:
        file_lines = csv.DictReader(file)
        for line in file_lines:
            address = Address.objects.create(line_1=line["line_1"],line_2=line["line_2"], city=line["city"],
                                             state=line["state"], zipcode=line["zip5"])
            owner = Owner.objects.get(id=1)
            Restaurant.objects.create(name=line["name"], telephone=line["telephone"],
                                    address=address, owner=owner)


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20150712_1949'),
    ]

    operations = [
        migrations.RunPython(data_migrate),
    ]
