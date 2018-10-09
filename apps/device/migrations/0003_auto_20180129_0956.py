# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-29 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_auto_20180127_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='do_type',
            new_name='status',
        ),
        migrations.AddField(
            model_name='device',
            name='is_destroy',
            field=models.BooleanField(default=0, verbose_name='是否报废'),
        ),
    ]
