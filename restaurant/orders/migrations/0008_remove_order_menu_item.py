# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20150710_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menu_item',
        ),
    ]
