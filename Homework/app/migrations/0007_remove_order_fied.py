# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_order_fied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='fied',
        ),
    ]