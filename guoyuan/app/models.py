from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title = models.CharField('名称', max_length=30)
    desc = models.CharField('描述', max_length=200, default='商品')
    flag = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='static/images/goods_type/')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'goods_type'

class Goods(models.Model):
    title = models.CharField('名称', max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture = models.ImageField(upload_to='static/images/goods/',
                                default='normal.png')
    isDelete = models.BooleanField(default=False)
    type = models.ForeignKey(GoodsType)
    desc = models.CharField('描述', max_length=200, default='商品')

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'goods'


class User(models.Model):
    username = models.CharField(max_length=16, null=False)
    password = models.CharField(max_length=16, null=False)
    email = models.EmailField(max_length=40, null=False)

    def __str__(self):
        return self.username


class Shoppingcar(models.Model):
    user_id = models.ForeignKey(User, null=False)
    goods_id = models.ForeignKey(Goods, null=False)
    date = models.DateTimeField(auto_now_add=True)
