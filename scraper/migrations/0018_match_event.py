# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0017_auto_20160428_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='event',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
