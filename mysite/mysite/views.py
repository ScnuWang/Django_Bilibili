from django.shortcuts import render_to_response
from read_statistics.utils import get_seven_read_data
from django. contrib.contenttypes.models import ContentType
from blog.models import Blog

def home(request):
	blog_content_type = ContentType.objects.get_for_model(Blog)
	sever_read_date,dates = get_seven_read_data(blog_content_type)
	context = {}
	context['sever_read_date'] = sever_read_date
	context['dates'] = dates
	return render_to_response("home.html",context)