from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 设置admin平台显示模式的内容
    list_display = ('id','tittle','context')
    # 排序：倒序在id 前面加负号
    ordering = ('id',)

# 可通过装饰器的方式代替：主要是为了防止要注册的类太多了不方便看
# admin.site.register(Article,ArticleAdmin)