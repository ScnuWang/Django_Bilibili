from django.db import models

# Create your models here.

class Article(models.Model):
    tittle = models.CharField(max_length=30)
    context = models.TextField()
