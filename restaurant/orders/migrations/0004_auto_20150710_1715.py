# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20150710_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='SC', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_parts',
            field=models.CharField(max_length=20, default='App', blank=True, choices=[('App', 'Appetizer'), ('Ent', 'Entree'), ('Des', 'Desert'), ('Dri', 'Drink')]),
        ),
    ]
