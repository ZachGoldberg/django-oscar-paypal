# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.AddField(
            model_name='expresstransaction',
            name='fee',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
        ),
    ]
