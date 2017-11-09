# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
fs = FileSystemStorage(location='C:/Users/wangz/Desktop/kingsite/static/media/')
ps = FileSystemStorage(location='C:/Users/wangz/Desktop/kingsite/static/head/')

class Hero(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField(null=False)
    date = models.DateField(null=False)
    user_num = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    desc = models.TextField(null=False)
    picture = models.ImageField(storage=fs)

    def __str__(self):
        return self.name


class Skin(models.Model):
    hero = models.ForeignKey(Hero)
    name = models.CharField(max_length=20)
    date = models.DateField(null=False)
    price = models.IntegerField()
    desc = models.TextField()
    picture = models.ImageField(storage=ps)

    def __str__(self):
        return self.id, self.name


class User(models.Model):
    name = models.CharField(max_length=10, null=False)
    gender = models.BooleanField(null=False)
    user_name = models.CharField(max_length=16, null=False)
    password = models.CharField(max_length=16, null=False)
    level = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    desc = models.TextField()
    picture = models.ImageField(ps)
    friends = models.ManyToManyField("self")
    money = models.IntegerField()
    diamond = models.IntegerField()
    stamps = models.IntegerField()

    def __str__(self):
        return self.name


class User_GET(models.Model):
    user = models.ForeignKey(User, null=False)
    heros = models.ForeignKey(Hero, on_delete=models.PROTECT, null=True)
    skins = models.ForeignKey(Skin, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.user


class Shopping_cart(models.Model):
    user = models.ForeignKey(User, null=False)
    heros = models.ForeignKey(Hero, on_delete=models.PROTECT, null=True)
    skins = models.ForeignKey(Skin, on_delete=models.PROTECT, null=True)