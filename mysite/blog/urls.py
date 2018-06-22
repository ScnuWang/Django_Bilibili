from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/blog/1
    path('<int:blog_pk>',views.blog_detail,name='blog_detail'),
    # localhost:8000/blog
    path('',views.blog_list,name='blog_list'),
    # localhost:8000/blog/type/1
    path('type/<int:blog_type_pk>',views.blog_with_type,name='blog_with_type'),
    # localhost:8000/blog/2018/06
    path('date/<int:year>/<int:month>',views.blog_with_date,name='blog_with_date')
]