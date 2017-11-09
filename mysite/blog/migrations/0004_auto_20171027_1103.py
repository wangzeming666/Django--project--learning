# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171027_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroinfo',
            old_name='gender',
            new_name='hgender',
        ),
        migrations.RenameField(
            model_name='heroinfo',
            old_name='launch_date',
            new_name='hlaunch_date',
        ),
        migrations.RenameField(
            model_name='heroinfo',
            old_name='name',
            new_name='hname',
        ),
        migrations.RenameField(
            model_name='skininfo',
            old_name='content',
            new_name='scontent',
        ),
        migrations.RenameField(
            model_name='skininfo',
            old_name='hero',
            new_name='shero',
        ),
        migrations.RemoveField(
            model_name='skininfo',
            name='name',
        ),
        migrations.AddField(
            model_name='skininfo',
            name='sname',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
