"""
    数据库表模型类
"""
from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称', max_length=30)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称', max_length=16)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('内容')
    pub = models.DateField('发布时间', auto_now_add=True)
    # on_delete解释：当子表中的某条数据删除后，关联的外键操作
    # on_delete = models.SET_NULL
    # 置空模式，删除时，外键字段被设置为空，前提就是blank=True, null=True,定义该字段时，允许为空。
    # 理解：删除关联数据（子表），与之关联的值设置默认值为null（父表中），这个前提需要父表中的字段可以为空。
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=None)  # 多对一（博客--类别）
    # 多对多关系，没有on_delete参数
    tag = models.ManyToManyField(Tag, verbose_name='标签')  # (多对多）

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    博客评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客', on_delete=None)  # (博客--评论:一对多)
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=240)
    pub = models.DateField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __unicode__(self):
        return self.content
