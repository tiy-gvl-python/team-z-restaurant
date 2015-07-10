# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20150710_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='plus_4',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
