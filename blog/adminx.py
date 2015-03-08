#coding:utf-8
import xadmin
from blog.models import BlogPost, BlogComment


class BlogPostAdmin(object):
    list_display = ('title')

xadmin.site.register(BlogPost)
