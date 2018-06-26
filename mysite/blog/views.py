from django.shortcuts import render,get_object_or_404,render_to_response
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType

from django.utils import timezone
from read_statistics.models import ReadNum,ReadDetail
from comment.models import Comment
from .models import Blog,BlogType

# 也可以在settings.py文件里面配置
each_page_blogs_num = 2

# 提取公共的代码
def blog_list_common_util(request,blog_list):

    paginator = Paginator(blog_list, each_page_blogs_num)  # 每页10篇
    page_num = request.GET.get('page', 1)  # 获取Get请求参数
    page_of_blog = paginator.get_page(page_num)  # 当前分页对象
    current_page_num = page_of_blog.number
    # 获取当前页面前后各两页的范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

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

    # 按照时间排序
    blogs_with_date = Blog.objects.dates('created_time', 'month', order='DESC') # 查询结果是日期类型
    # 这里如果使用annotate比较麻烦，因为这里是是时间对象列表
    blogs_with_date_dict = {}
    for blog_date in blogs_with_date:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blogs_with_date_dict[blog_date] = blog_count


    # 博客分类统计
    '''
    # 给类新增属性：blog_count
    blog_count_with_type=[]
    for blog_type in BlogType.objects.all():
        blog_type.blog_count = Blog.objects.filter(blogtype=blog_type).count()
        blog_count_with_type.append(blog_type)
    '''
    # blog 是关联对象的小写 blog_count属性可以自定义，但是不能和模型已有对象相同
    blog_count_with_type = BlogType.objects.annotate(blog_count=Count('blog'))

    context = {}
    context['page_range'] = page_range
    context['page_of_blog'] = page_of_blog
    context['blogtypes'] = blog_count_with_type
    context['blogs_with_date'] = blogs_with_date_dict

    return context



# Create your views here.
def blog_list(request):
    blog_all_list = Blog.objects.all()
    context = blog_list_common_util(request,blog_all_list)
    return render(request,"blog/blog_list.html",context)


def blog_detail(request,blog_pk):

    # 上一篇文章，下一篇文章，按实际排序
    blog = get_object_or_404(Blog,pk=blog_pk)
    # 阅读量计数
    # if not request.COOKIES.get('blog_%s_read' % blog_pk):
    #     blog.read_num += 1
    #     blog.save()
    # 阅读量优化，新建一个模型记录阅读次数，与博客分开
    # if not request.COOKIES.get('blog_%s_read' % blog_pk):
        # if ReadNum.objects.filter(blog=blog).count():
        #     # 存在计数与博客之间的记录
        #     readnum = ReadNum.objects.get(blog=blog)
        # else:
        #     # 不存在
        #     readnum = ReadNum(blog=blog)
        # readnum.read_num +=1
        # readnum.save()

    # 使用ContentType
    ct = ContentType.objects.get_for_model(Blog)
    if not request.COOKIES.get('blog_%s_read' % blog_pk):
        # if ReadNum.objects.filter(content_type=ct, object_id=blog.pk).count():
        #     readnum = ReadNum.objects.get(content_type=ct, object_id=blog.pk)
        # else:
        #     readnum = ReadNum(content_type=ct, object_id=blog.pk)

        # 用下面这个替代上面的
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=blog.pk)
        readnum.read_num += 1
        readnum.save()

        date = timezone.now().date()
        # if ReadDetail.objects.filter(content_type=ct, object_id=blog.pk, date= date).count():
        #     readDetail = ReadDetail.objects.get(content_type=ct, object_id=blog.pk, date= date)
        # else:
        #     readDetail = ReadDetail(content_type=ct, object_id=blog.pk, date= date)

        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=blog.pk, date= date)
        readDetail.read_num += 1
        readDetail.save()

    # 处理博客评论列表
    comment_list = Comment.objects.filter(content_type=ct, object_id=blog.pk)



    # 当前博客的时间
    current_blog_create_time = blog.created_time
    # created_time__gt：表当前时间大的 last()：最后一条 first()；第一条
    previous_blog = Blog.objects.filter(created_time__gt=current_blog_create_time).last()
    next_blog = Blog.objects.filter(created_time__lt=current_blog_create_time).first()
    # 当前博客

    context = {}
    context['previous_blog'] = previous_blog
    context['next_blog'] = next_blog
    context['blog'] = blog
    context['comment_list'] = comment_list
    # 设置Cookie 用于统计阅读次数
    response = render(request,"blog/blog_detail.html",context)
    response.set_cookie('blog_%s_read' % blog_pk,'True')
    return response


# 根据类型获取博客列表
def blog_with_type(request,blog_type_pk):

    blogtype = get_object_or_404(BlogType,pk=blog_type_pk)
    blog_all_list = Blog.objects.filter(blogtype=blogtype)
    context = blog_list_common_util(request,blog_all_list)
    context['blogtype'] = blogtype
    return  render(request,"blog/blog_with_type.html",context)

# 根据时间获取博客列表
def blog_with_date(request,year,month):
    blog_list_with_date = Blog.objects.filter(created_time__year=year,created_time__month=month)
    context = blog_list_common_util(request, blog_list_with_date)
    context['blog_with_date'] = "%s年 %s月" % (year,month)
    return render(request,"blog/blog_with_date.html", context)