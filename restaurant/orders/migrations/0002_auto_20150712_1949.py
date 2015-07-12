# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
from django.contrib.auth.models import User

from django.db import models, migrations
from orders.models import Owner


def data_migrate(x, y):
    with open('../data/owner.csv') as file:
        file_lines = csv.DictReader(file)
        for line in file_lines:
            user = User(username=line["username"])
            user.set_password("owner")
            user.save()
            Owner.objects.create(user=user, name=line["name"], telephone=line["telephone"])




class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data_migrate),
    ]
