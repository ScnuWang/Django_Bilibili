from django.contrib import admin
from .models import ReadNum

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num','content_object')
    ordering = ('id',)
