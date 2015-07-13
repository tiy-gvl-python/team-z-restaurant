# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_crypto_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='crypto_order',
            field=models.OneToOneField(related_name='order', to='django_cryptocoin.CryptoOrder', null=True),
        ),
    ]
