# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations

from orders.models import MenuItem

def data_migrate(x, y):
    with open('../data/menu.csv') as file:
        file_lines = csv.DictReader(file)
        for line in file_lines:
            MenuItem.objects.create(title=line["title"], description=line["description"],
                                    price=line["cost"], menu_parts=line["menu_parts"])


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20150712_1949'),
    ]

    operations = [
        migrations.RunPython(data_migrate),
    ]
