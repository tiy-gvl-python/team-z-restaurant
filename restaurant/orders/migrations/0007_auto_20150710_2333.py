# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20150710_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='food_item',
            new_name='menu_item',
        ),
    ]
