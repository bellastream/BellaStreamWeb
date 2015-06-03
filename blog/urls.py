from django.conf.urls import *
from blog.views import blog_detail_view, blog_archive_view

urlpatterns = patterns('',
		url(r'^(\d{1,})/?$', blog_detail_view),
		url(r'^$', blog_archive_view),
	)
