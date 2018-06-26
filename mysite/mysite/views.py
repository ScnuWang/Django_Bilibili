import datetime
from django.shortcuts import render,redirect
from django. contrib.contenttypes.models import ContentType
from django.contrib import auth
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.urls import reverse
from blog.models import Blog
from read_statistics.utils import get_seven_read_data,get_today_hot_read_data,get_yestoday_hot_read_data

# 利用ContentType的反向关系
def get_sevendays_hot_read_data():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    # 同一篇可能出现在多天的热门文章 --》分组统计
    # 注意这里readDetail__read_num 是两个下划线，表示取属性
    blogs = Blog.objects.filter(readDetail__date__lt=today, readDetail__date__gte=date).values('pk', 'tittle') \
        .annotate(read_num_sum=Sum('readDetail__read_num')) \
        .order_by('-read_num_sum')
    return blogs[:7]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    sever_read_date, dates = get_seven_read_data(blog_content_type)
    # 使用缓存
    sevendays_hot_read_data = cache.get('sevendays_hot_read_data')
    if sevendays_hot_read_data is None:
        sevendays_hot_read_data = get_sevendays_hot_read_data()
        cache.set('sevendays_hot_read_data', sevendays_hot_read_data, 60 * 60)
    else:
        print("使用缓存获取数据")

    context = {}
    context['sever_read_date'] = sever_read_date
    context['hot_read_data'] = get_today_hot_read_data(blog_content_type)
    context['yestoday_hot_read_data'] = get_yestoday_hot_read_data(blog_content_type)
    context['sevendays_hot_read_data'] = sevendays_hot_read_data
    context['dates'] = dates
    return render(request,"home.html", context)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER',reverse('home'))
    if user is not None:
        auth.login(request, user)
        # Redirect to a success page.
        return redirect(referer)
    else:
        # Return an 'invalid login' error message.
        return render(request,'error.html',{'message':'用户名或者密码错误！！！'})