# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-11 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_users', '0006_auto_20170811_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuser',
            name='card_id',
            field=models.CharField(blank=True, max_length=8, verbose_name='id банковской карты'),
        ),
    ]
