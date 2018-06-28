from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/comment/update_comment
    path('update_comment',views.update_comment,name='update_comment'),
    path('blog_comment_list',views.blog_comment_list,name='blog_comment_list'),
]