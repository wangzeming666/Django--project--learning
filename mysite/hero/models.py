from django.db import models

# Create your models here.
class HeroInfo(models.Model):
    hname = models.CharField('英雄名',unique=True,db_index=True,max_length=20, db_column='name')
    hgender = models.BooleanField('性别',default=True)
    hlaunch_date = models.DateField('发布日期',null=True,db_column='launch_date')
    hnumber_people = models.IntegerField('使用人数')
    hprice = models.DecimalField('商城价格',max_digits=8,decimal_places=2)
    # 用于逻辑删除
    isDelete = models.BooleanField('是否删除',default=False)
    # 用于str(obj)会自动调用
    def __str__(self):
        return self.hname

class SkinInfo(models.Model):
    sname = models.CharField(max_length=20)
    scontent = models.CharField(max_length=200)
    shero = models.ForeignKey(HeroInfo)
    isDelete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sname

class Meta():
    # 默认的表名是：应用名_模型名
    db_table = 'heroinfo'
    # 设置排序的字段
    ordering = ['id']
