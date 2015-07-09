# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='owner',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
    ]
