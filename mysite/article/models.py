from django.db import models

# Create your models here.

class Article(models.Model):
    tittle = models.CharField(max_length=30)
    context = models.TextField()

    #
    def __str__(self):
        return "<Article: %s>" % self.tittle
