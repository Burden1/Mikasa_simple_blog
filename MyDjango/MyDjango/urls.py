"""
    配置文件路由
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from MyBlog.views import get_blogs, get_details

urlpatterns = [
    # path(..)是Django2.0的写法，url(...)是Django1.0的写法
    path('admin/', admin.site.urls),
    url(r'^blog/$', get_blogs),
    url(r'^detail/(\d+)/$', get_details, name='blog_get_detail'),
]
