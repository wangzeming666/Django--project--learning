# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 01:36
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='picture',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media'), upload_to=''),
        ),
    ]
