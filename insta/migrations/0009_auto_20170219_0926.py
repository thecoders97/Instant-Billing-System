# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 03:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_auto_20170219_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pnotes',
            name='pmonth',
        ),
        migrations.RemoveField(
            model_name='pnotes',
            name='pyear',
        ),
    ]
