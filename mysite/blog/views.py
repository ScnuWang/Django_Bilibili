from django.shortcuts import render,render_to_response,get_object_or_404,get_list_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator
# Create your views here.
def blog_list(request):
    blog_all_list = Blog.objects.all();
    paginator = Paginator(blog_all_list,10)# 每页10篇
    page_num = request.GET.get('page',1)# 获取Get请求参数
    page_of_blog = paginator.get_page(page_num)

    context = {}
    context['page_of_blog'] = page_of_blog
    context['blogtypes'] = BlogType.objects.all()
    return render_to_response("blog/blog_list.html",context)


def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response("blog/blog_detail.html",context)

def blog_with_type(request,blog_type_pk):
    context = {}
    blogtype = get_object_or_404(BlogType,pk=blog_type_pk)
    # 获取分类名称
    context['blogtype'] = blogtype
    context['blogs'] = Blog.objects.filter(blogtype=blogtype)
    context['blogtypes'] = BlogType.objects.all()
    return  render_to_response("blog/blog_with_type.html",context)