# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_users', '0002_stuser_shelves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuser',
            name='bought_books',
            field=models.ManyToManyField(blank=True, to='books.Book'),
        ),
    ]