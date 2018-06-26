from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/comment/update_comment
    path('update_comment',views.update_comment,name='update_comment'),
    path('comment_list',views.get_comment_list,name='comment_list'),
]