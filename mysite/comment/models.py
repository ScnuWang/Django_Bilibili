from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    comment_user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    comment_content = models.TextField()
    comment_datatime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_datatime']
