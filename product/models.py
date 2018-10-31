from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField('项目名称',max_length=64)
    productdesc=models.CharField('项目描述',max_length=200)
    producter=models.CharField('项目负责人',max_length=200)
    create_time=models.DateTimeField('创建时间',auto_now=True)
    class Meta:
        verbose_name='项目管理'
        verbose_name_plural='项目管理'
    def __str__(self):
        return self.productname