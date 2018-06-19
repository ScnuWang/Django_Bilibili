from django.db import models

# Create your models here.
# 修改模型之后需要重新执行迁移数据库，再执行之前，先备份数据库
class Article(models.Model):
    tittle = models.CharField(max_length=30)
    context = models.TextField()


    def __str__(self):
        return "<Article: %s>" % self.tittle
