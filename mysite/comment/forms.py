from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content_type = forms.CharField(widget=forms.HiddenInput)
    comment_content = forms.CharField(label='',widget=CKEditorWidget(config_name='comment_ckeditor'))

    # 校验用户是否登录，通过这种方式传递user
    def __init__(self,*args,**kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm,self).__init__(*args,**kwargs)


    # 校验
    def clean(self):
        # 用户是否登录
        if not self.user.is_authenticated:
            raise forms.ValidationError('请先登录再评论')
        else:
            self.cleaned_data['user'] = self.user

        # 评论对象是否存在
        try:
            object_id = self.cleaned_data['object_id']
            content_type = self.cleaned_data['content_type']
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论对象不存在')

        self.cleaned_data['model_obj'] = model_obj
        return self.cleaned_data

