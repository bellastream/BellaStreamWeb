# -*- coding:utf-8 -*-
from django.db import models


POST_TYPE = ['', '', '']


class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField(default="", verbose_name="内容")
	type = models.ForeignKey(BlogType)
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


class BlogType(models.Model):
	name = models.CharField(max_length=50, default="", verbose_name="名字")
