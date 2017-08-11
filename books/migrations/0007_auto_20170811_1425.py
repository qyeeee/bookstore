# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-11 11:25
from __future__ import unicode_literals

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20170810_1959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.get_image_path, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(blank=True, max_length=2500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.get_image_path, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название книги'),
        ),
    ]
