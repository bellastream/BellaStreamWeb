from django.conf.urls import include, url
from django.conf import settings
#from django.contrib import admin
import xadmin
xadmin.autodiscover()
#from xadmin.plugins import xversion
#xversion.registe_models()


urlpatterns = [
    # Examples:
    #url(r'^$', 'BellaStreamWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'BellaStreamWeb.views.home'),
    url(r'^admin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^blog/', include('blog.urls')),
]

if settings.DEBUG is False:
	urlpatterns += [
		url(r'^statics/(.*)$', 'django.views.static.serve', {'document_root': settings.TEMPLATE_ROOT}),
]
