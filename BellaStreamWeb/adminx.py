#coding:utf-8
from django.contrib import admin

from blog.models import BlogPost, BlogComment, BlogPostAdmin

class BlogPostAdmin():
	list_display = ('title', 'timestamp')	

# Register your models here.
xadmin.site.register(BlogPost,BlogPostAdmin)
xadmin.site.register(BlogComment)
