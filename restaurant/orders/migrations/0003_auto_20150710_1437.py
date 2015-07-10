# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20150709_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, to='orders.Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='food_item',
            field=models.ManyToManyField(to='orders.MenuItem'),
        ),
    ]
