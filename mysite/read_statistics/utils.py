import datetime
from django.utils import timezone
from django.db.models import Sum
from .models import ReadDetail

# 获取最近7天的阅读量数据
def get_seven_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(7,0,-1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        readDetail = ReadDetail.objects.filter(content_type=content_type,date=date)
        result = readDetail.aggregate(read_num_sum = Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)

    return read_nums,dates

# 当天的阅读量数据
def get_today_hot_read_data(content_type):
    today = timezone.now().date()
    readDetail = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    return readDetail[:7]

# 昨天的阅读量数据
def get_yestoday_hot_read_data(content_type):
    today = timezone.now().date()
    yestoday = today - datetime.timedelta(days=1)
    readDetail = ReadDetail.objects.filter(content_type=content_type, date=yestoday).order_by('-read_num')
    return readDetail[:7]

# 7 天热门数据:  直接使用上面的方式获取会报错