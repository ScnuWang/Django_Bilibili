from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 修改模型之后需要重新执行迁移数据库，再执行之前，先备份数据库
class Article(models.Model):
    tittle = models.CharField(max_length=30,verbose_name="标题")
    context = models.TextField(verbose_name="内容")
    # 注意二者的区别
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间") # 在创建数据迁移文件的时候不能自动添加时间?
    last_update_time = models.DateTimeField(auto_now=True,verbose_name="上次修改时间")
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1,verbose_name="作者")
    is_delete = models.BooleanField(default=False,verbose_name="是否删除")
    read_num = models.IntegerField(default=0,verbose_name="阅读次数")



    def __str__(self):
        return "<Article: %s>" % self.tittle
