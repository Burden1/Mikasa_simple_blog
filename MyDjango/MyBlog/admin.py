"""
    # Register your models here.
    django自带的后台管理系统
    在这儿注册你的模型
"""
from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'pub')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'content', 'pub')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
