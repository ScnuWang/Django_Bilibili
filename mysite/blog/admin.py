from django.contrib import admin
from .models import Blog,BlogType
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','tittle','blogtype','author','created_time','last_update_time')
    ordering = ('id',)

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'typename')
    ordering = ('id',)
