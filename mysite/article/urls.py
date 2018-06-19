from django.urls import path
# 同一个目录，引用用.代替
from . import views

urlpatterns = [
    # localhost:8000/article/1
    # 注意这里给变量指定类型的格式
	path('<int:article_id>',views.article_detail,name='article_detail'),
    # localhost:8000/article
    path('',views.article_list,name='article_list'),
]