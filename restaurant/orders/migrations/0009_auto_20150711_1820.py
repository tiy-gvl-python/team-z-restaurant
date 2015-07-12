# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_order_menu_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOption',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('quantity', models.IntegerField(default=1)),
                ('menu_item', models.ForeignKey(to='orders.MenuItem')),
                ('order', models.ForeignKey(to='orders.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='menu_item',
            field=models.ManyToManyField(to='orders.MenuItem', through='orders.CartOption'),
        ),
    ]
