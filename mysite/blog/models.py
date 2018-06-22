from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class BlogType(models.Model):
    typename = models.CharField(max_length=15)

    def __str__(self):
        return self.typename

class Blog(models.Model):
    tittle = models.CharField(max_length=50)
    blogtype = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    read_num = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    # 定义排序
    class Meta:
        ordering=['-created_time',]

