# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-11 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_users', '0005_stuser_cards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuser',
            name='cards',
        ),
        migrations.DeleteModel(
            name='identifikator',
        ),
    ]