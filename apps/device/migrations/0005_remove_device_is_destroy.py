# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_auto_20180129_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='is_destroy',
        ),
    ]
