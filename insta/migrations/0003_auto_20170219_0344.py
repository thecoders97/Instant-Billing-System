# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20170219_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='modified_at',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.TextField(null=True),
        ),
    ]
