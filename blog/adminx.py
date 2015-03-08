# coding:utf-8
import xadmin
from django import forms
from blog.models import BlogPost, BlogComment
from BellaStreamWeb import settings


class TinymceWidget(forms.Textarea):
    class Media:
        js = (
                settings.STATIC_URL + 'js/tinymce/tinymce.min.js',
                settings.STATIC_URL + 'js/tinymce_load.js'
        )


#自定义UserPost表单
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': TinymceWidget(attrs={'rows': 30}),
        }


class BlogPostAdmin(object):
    list_display = ['title', 'type', 'last_modified']
    form = BlogPostForm


class BlogCommentAdmin(object):
    list_display = ['post', 'author', 'create_time']


xadmin.site.register(BlogPost, BlogPostAdmin)
xadmin.site.register(BlogComment, BlogCommentAdmin)

