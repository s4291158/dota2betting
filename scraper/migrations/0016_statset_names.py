# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0015_auto_20160427_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='statset',
            name='names',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
