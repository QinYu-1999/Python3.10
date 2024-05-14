from django.db import models


class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16, db_index=True)  # 索引
    age = models.IntegerField(verbose_name='年龄')
    ct_date = models.DateTimeField(verbose_name='创建时间', auto_now=True,null=True)
    # up_date = models.DateField(verbose_name='日期', null=True)
    email = models.CharField(verbose_name='邮箱', max_length=128, unique=True, null=True)  # unique唯一索引
    amount = models.DecimalField(verbose_name='工资', max_digits=10, decimal_places=2, default=0)  # 最长10，保留2位小数


class Goods(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    # detail = models.CharField(verbose_name='详细信息',max_length=255) #charFied 0~255字符
    detail = models.TextField('详细信息')
    price = models.PositiveIntegerField(verbose_name='价格')
    count = models.IntegerField(verbose_name='库存', default=0)
