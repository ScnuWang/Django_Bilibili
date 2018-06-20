from django.shortcuts import render,render_to_response,get_object_or_404,get_list_or_404
from .models import Blog,BlogType

# Create your views here.
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response("blog_list.html",context)


def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response("blog_detail.html",context)

def blog_with_type(request,blog_type_pk):
    context = {}
    blogtype = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blogtype=blogtype)
    # 获取分类名称
    context['blogtype'] = blogtype
    return  render_to_response("blog_with_type.html",context)