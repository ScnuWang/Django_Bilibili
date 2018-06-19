from django.shortcuts import render,render_to_response,get_object_or_404,get_list_or_404
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.

def article_detail(request,article_id): # 虽然这个request 没有使用，但是还是要传
    article = get_object_or_404(Article,id=article_id)
    context = {}
    context['article_obj'] = article
    return render_to_response('article_detail.html', context)

    # try:
    #     article = Article.objects.get(id=article_id)
    #     context = {}
    #     context['article_obj'] = article
    #     return render_to_response('article_detail.html',context)
    # except Article.DoesNotExist: # 要用Article.
    #     raise Http404("文章不存在！")

def article_list(request):
    article_list = get_list_or_404(Article,is_delete = False)# 自带过滤器，is_delete是模型字段
    context = {}
    context['article_list'] = article_list
    return render_to_response('article_list.html', context)
