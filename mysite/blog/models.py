from django.db import models

# Create your models here.
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hlaunch_date = models.DateTimeField()
    birthday = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hname

class SkinInfo(models.Model):
    sname = models.CharField(max_length=20)
    scontent = models.CharField(max_length=200)
    shero = models.ForeignKey(HeroInfo)

    def __str__(self):
        return self.sname
