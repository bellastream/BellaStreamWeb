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
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'BellaStreamWeb.views.home'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^blog/', include('blog.urls')),
]


