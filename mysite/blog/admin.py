from django.contrib import admin
from .models import Blog,BlogType
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 这里可显示的字段是模型的字段属性，不带额外参数的方法名（显示结果是方法返回值）
    list_display = ('id','tittle','blogtype','author','get_read_num','created_time','last_update_time')
    ordering = ('id',)

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'typename')
    ordering = ('id',)
