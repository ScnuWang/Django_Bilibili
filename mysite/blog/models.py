from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogType(models.Model):
    typename = models.CharField(max_length=15)

    def __str__(self):
        return self.typename

class Blog(models.Model):
    tittle = models.CharField(max_length=50)
    blogtype = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

