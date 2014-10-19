from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    #url(r'^$', 'BellaStreamWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'BellaStreamWeb.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
]

if settings.DEBUG is False:
	urlpatterns += [
		url(r'^templates/(.*)$', 'django.views.static.serve', {'document_root': settings.TEMPLATE_ROOT}),
]
