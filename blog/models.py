# -*- coding:utf-8 -*-
from django.db import models


POST_TYPE = (
    ('DIARY', '记忆.'),
    ('TRAVEL', '时光.'),
    ('IMAGE', '碎片'),
	('OTHER', '弦.'),
)

BLOG_UPLOAD_ROOT = "pictures"

class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(upload_to=BLOG_UPLOAD_ROOT, null=True, verbose_name="配图")
	content = models.TextField(default="", verbose_name="内容")
	type = models.CharField(max_length=10, choices=POST_TYPE, verbose_name="类别")
	create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	last_modified = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-last_modified']


class BlogComment(models.Model):
	post = models.ForeignKey(BlogPost)
	author = models.CharField(max_length=30, default="", verbose_name="名字")
	email = models.EmailField()
	content = models.TextField(default="", verbose_name="内容")
	create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

	def __unicode__(self):
		return self.post.title + '-' + self.author

	class Meta:
		ordering = ['create_time']
