# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fied',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
