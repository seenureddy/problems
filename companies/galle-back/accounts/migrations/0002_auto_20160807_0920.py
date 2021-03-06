# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 09:20
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_image, verbose_name='Upload Article Picture'),
        ),
        migrations.AddField(
            model_name='article',
            name='optinal_image',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_image, verbose_name='Upload Article Picture'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
