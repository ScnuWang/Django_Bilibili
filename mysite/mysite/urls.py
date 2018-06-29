"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# 同一个目录，引用用.代替
from .views import home,login,regist
# 2.x 使用的path,正则表达式使用re_path;
# 1.x 使用的版本是url，
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',home,name='home'),
    path('admin/', admin.site.urls),
	# path('article/',include('article.urls')),
	path('blog/',include('blog.urls')),
	path('ckeditor',include('ckeditor_uploader.urls')),
	path('comment/',include('comment.urls')),
	path('login/',login,name='login'),
	path('regist/',regist,name='regist'),
]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
