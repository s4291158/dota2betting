# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0011_auto_20160427_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamstatset',
            options={},
        ),
        migrations.AlterField(
            model_name='teamstat',
            name='teamstatset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.TeamstatSet'),
        ),
    ]
