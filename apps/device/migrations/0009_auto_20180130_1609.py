# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0008_auto_20180130_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceattr',
            name='move_num',
        ),
        migrations.AddField(
            model_name='deviceattr',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='描述'),
        ),
    ]
