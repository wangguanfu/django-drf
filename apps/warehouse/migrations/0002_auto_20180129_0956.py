# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-29 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='仓库类型'),
        ),
    ]
