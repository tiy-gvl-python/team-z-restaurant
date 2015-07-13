# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_cryptocoin', '__first__'),
        ('orders', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='crypto_order',
            field=models.OneToOneField(related_name='order', default=1, to='django_cryptocoin.CryptoOrder'),
            preserve_default=False,
        ),
    ]
