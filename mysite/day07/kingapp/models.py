from django.db import models

# Create your models here.

class HeroInfo(models.Model):
    #hid = models.AutoField(primary_key=True, db_column='id')
    #db_index=True 在此字段上创建索引
    #unique=True 此字段不允许重复
    hname = models.CharField('英雄名',unique=True,db_index=True,max_length=20, db_column='name')
    hgender = models.BooleanField('性别',default=True)
    #null=True 该字段允许为空
    hlaunch_date = models.DateField('发布日期',null=True,db_column='launch_date')
    hnumber_people = models.IntegerField('使用人数')
    hprice = models.DecimalField('商城价格',max_digits=8,decimal_places=2)
    # 用于逻辑删除
    isDelete = models.BooleanField('是否删除',default=False)
    # 用于str(obj)会自动调用
    def __str__(self):
        return self.hname

    #Meta类，定义元数据
    class Meta():
        # 默认的表名是：应用名_模型名
        db_table = 'heroinfo'
        # 设置排序的字段
        ordering = ['-id']


class SkinInfo(models.Model):
    sname = models.CharField(max_length=20, db_column='name')
    scontent = models.CharField(max_length=1000, db_column='content')
    shero = models.ForeignKey(HeroInfo, db_column='hero_id')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.sname
