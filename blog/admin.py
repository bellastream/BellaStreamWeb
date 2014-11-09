from django.contrib import admin
from blog.models import BlogPost, BlogComment, BlogPostAdmin

# Register your models here.
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogComment)
