from django.conf.urls import *
from blog.views import archivePage
from blog.views import detailPage

urlpatterns = patterns('',
		url(r'^(\d{1,})/?$', detailPage),
		url(r'^$', archivePage),
	)
