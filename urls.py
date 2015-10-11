from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = [
    # Examples:
    #url(r'^$', 'BellaStreamWeb.views.home', name='home'),

    url(r'^$', 'views.home_view'),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^music/', 'views.music_view'),
    url(r'^about/', 'views.about_view'),
    url(r'^wechat/', include('wechat.urls')),
]


