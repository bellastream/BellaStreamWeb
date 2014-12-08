from django.db import models
from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['-timestamp']
	

class BlogComment(models.Model):
	post = models.ForeignKey(BlogPost)
	author = models.CharField(max_length = 30)
	email = models.EmailField()
	body = models.TextField()
	timestamp = models.DateTimeField()
	def __unicode__(self):
		return self.post.title + '-' + self.author 
	class Meta:
		ordering = ['timestamp']


