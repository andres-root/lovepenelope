# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_twitterconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterconfiguration',
            name='account',
            field=models.CharField(default='@Penelope', max_length=200),
            preserve_default=False,
        ),
    ]
