#coding:utf-8
import xadmin
from blog.models import BlogPost, BlogComment, BlogType

class BlogPostAdmin(object):
    list_display = ('title', 'type', 'last_modified')

class BlogCommentAdmin(object):
    list_display = ('post', 'author', 'create_time')

class BlogTypeAdmin(object):
    list_display = ('name')

xadmin.site.register(BlogPost, BlogPostAdmin)
xadmin.site.register(BlogComment, BlogCommentAdmin)
xadmin.site.register(BlogType, BlogTypeAdmin)

