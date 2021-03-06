# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField()),
                ('hlaunch_date', models.DateTimeField()),
                ('birthday', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('scontent', models.CharField(max_length=200)),
                ('shero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.HeroInfo')),
            ],
        ),
    ]
