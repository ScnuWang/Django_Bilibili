from django.db import models
from django.contrib.auth.models import User
from read_statistics.models import ReadNum
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadDetail

# 可以在shell模式下通过blogtype对象的blog_set获取blog对象列表
class BlogType(models.Model):
    typename = models.CharField(max_length=15)

    def __str__(self):
        return self.typename

class Blog(models.Model):
    tittle = models.CharField(max_length=50)
    # 外键是一对多或者多对一的关系
    blogtype = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    readDetail = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(Blog)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

    # 定义排序
    class Meta:
        ordering=['-created_time',]
