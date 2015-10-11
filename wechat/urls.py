from django.conf.urls import *
from views import get_wechat_view

urlpatterns = patterns('',
		url(r'^get/', get_wechat_view),
	)
