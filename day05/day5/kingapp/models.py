from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20, db_column="uname")
    upwd = models.CharField(max_length=64, db_column="upwd")
