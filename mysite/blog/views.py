from django.shortcuts import render,render_to_response,get_object_or_404,get_list_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator

# 也可以在settings.py文件里面配置
each_page_blogs_num = 2

# Create your views here.
def blog_list(request):
    blog_all_list = Blog.objects.all();
    paginator = Paginator(blog_all_list,each_page_blogs_num)# 每页10篇
    page_num = request.GET.get('page',1)# 获取Get请求参数
    page_of_blog = paginator.get_page(page_num)# 当前分页对象
    current_page_num = page_of_blog.number
    # 获取当前页面前后各两页的范围
    page_range = list(range(max(current_page_num-2,1),current_page_num))+ list(range(current_page_num,min(current_page_num+2,paginator.num_pages)+1))

    # 添加省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 添加第一页和最后一页
    if page_range[0] != 1 :
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages :
        page_range.append(paginator.num_pages)


    context = {}
    context['page_range'] = page_range
    context['page_of_blog'] = page_of_blog
    context['blogtypes'] = BlogType.objects.all()
    return render_to_response("blog/blog_list.html",context)


def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response("blog/blog_detail.html",context)

def blog_with_type(request,blog_type_pk):

    blogtype = get_object_or_404(BlogType,pk=blog_type_pk)
    blog_all_list = Blog.objects.filter(blogtype=blogtype)

    paginator = Paginator(blog_all_list, each_page_blogs_num)  # 每页10篇
    page_num = request.GET.get('page', 1)  # 获取Get请求参数
    page_of_blog = paginator.get_page(page_num)

    current_page_num = page_of_blog.number
    # 获取当前页面前后各两页的范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
        range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    # 添加省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 添加第一页和最后一页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    context = {}
    context['page_range'] = page_range
    context['blogtype'] = blogtype
    context['page_of_blog'] = page_of_blog
    context['blogtypes'] = BlogType.objects.all()
    return  render_to_response("blog/blog_with_type.html",context)