# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_pnotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pnotes',
            name='pdates',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
