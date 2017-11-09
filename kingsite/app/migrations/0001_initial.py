# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.BooleanField()),
                ('date', models.DateField()),
                ('user_num', models.IntegerField()),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('picture', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('desc', models.TextField()),
                ('picture', models.CharField(max_length=50)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Hero')),
            ],
        ),
    ]