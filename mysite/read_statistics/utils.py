import datetime
from django.utils import timezone
from django.db.models import Sum
from .models import ReadDetail

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