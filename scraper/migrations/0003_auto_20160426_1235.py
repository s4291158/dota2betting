# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20160426_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='bestof',
            field=models.IntegerField(default=1),
        ),
    ]