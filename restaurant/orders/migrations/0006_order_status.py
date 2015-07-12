# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20150712_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('In Cart', 'In Cart'), ('Payment Received', 'Payment Received'), ('Being Cooked', 'Being Cooked'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=50, default='In Cart'),
        ),
    ]
