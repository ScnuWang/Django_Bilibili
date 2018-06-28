from django.shortcuts import redirect,reverse,render
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from blog.models import Blog
from .forms import CommentForm
from .models import Comment
# Create your views here.
def update_comment(request):
    # referer = request.META.get('HTTP_REFERER', reverse('home'))

    # 数据检查
    # if not request.user.is_authenticated:
    #     return render(request, 'error.html', {'message': '请先登录再评论','redirect_to':referer})

    # comment_content = request.POST.get('comment_content').strip()
    # if comment_content == '':
    #     return render(request,'error.html',{'message':'评论为空！！！','redirect_to':referer})

    # try:
    #     object_id = int(request.POST.get('object_id'))
    #     content_type = request.POST.get('content_type')
    #     model_class = ContentType.objects.get(model=content_type).model_class()
    #     model_obj = model_class.objects.get(pk=object_id)
    # except Exception as error:
    #     return render(request, 'error.html', {'message': '评论对象不存在！！！','redirect_to':referer})

    comment_form = CommentForm(request.POST,user=request.user)
    # 响应Ajax
    data = {}

    if comment_form.is_valid():
        comment = Comment()
        comment.comment_user = request.user
        comment.comment_content = comment_form.cleaned_data['comment_content']
        comment.content_object = comment_form.cleaned_data['model_obj']
        comment.save()
        # return redirect(referer)
        data['status'] = 'SUCCESS'
        data['username'] = comment.comment_user.username
        data['comment_time'] = comment.comment_datatime.strftime('%Y-%m-%d %H:%M:%S')
        data['comment_content'] = comment.comment_content
    else:
        # return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)


def blog_comment_list(request):
    blog_pk = request.GET.get('blog_pk')
    blog = get_object_or_404(Blog, pk=blog_pk)
    blog_content_type = ContentType.objects.get_for_model(Blog)
    comment_list = Comment.objects.filter(content_type=blog_content_type, object_id=blog.pk)
    return JsonResponse(data=comment_list)

