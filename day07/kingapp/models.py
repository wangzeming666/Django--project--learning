from django.db import models
class HeroInfo(models.Model):
    hname = models.CharField('英雄名',unique=True,db_index=True,max_length=20, db_column='name')
    hgender = models.BooleanField('性别',default=True)
    hlaunch_date = models.DateField('发布日期',null=True,db_column='launch_date')
    hnumber_people = models.IntegerField('使用人数')
    hprice = models.DecimalField('商城价格',max_digits=8,decimal_places=2)
    isDelete = models.BooleanField('是否删除',default=False)
    def __str__(self):
        return self.hname
    class Meta():
        db_table = 'heroinfo'
        ordering = ['id']

class SkinInfo(models.Model):
    sname = models.CharField(max_length=20, db_column='name')
    scontent = models.CharField(max_length=1000, db_column='content')
    shero = models.ForeignKey(HeroInfo, db_column='hero_id')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.sname

