# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 02:24
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
                ('hname', models.CharField(db_column='name', db_index=True, max_length=20, unique=True, verbose_name='英雄名')),
                ('hgender', models.BooleanField(default=True, verbose_name='性别')),
                ('hlaunch_date', models.DateField(db_column='launch_date', null=True, verbose_name='发布日期')),
                ('hnumber_people', models.IntegerField(verbose_name='使用人数')),
                ('hprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商城价格')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'heroinfo',
            },
        ),
        migrations.CreateModel(
            name='SkinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(db_column='name', max_length=20)),
                ('scontent', models.CharField(db_column='content', max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
                ('shero', models.ForeignKey(db_column='hero_id', on_delete=django.db.models.deletion.CASCADE, to='kingapp.HeroInfo')),
            ],
        ),
    ]