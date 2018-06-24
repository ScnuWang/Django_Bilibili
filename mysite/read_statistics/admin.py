from django.contrib import admin
from .models import ReadNum,ReadDetail

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num','content_object')
    ordering = ('id',)

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'read_num','content_object')
    ordering = ('id',)