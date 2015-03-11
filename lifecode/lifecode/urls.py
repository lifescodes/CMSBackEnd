from django.conf.urls import patterns, include, url
from django.contrib import admin
from lifecode import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lifecode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^upload/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.base.UPLOAD_ROOT,
        }),

    url(r'^v1/admin/', include(admin.site.urls)),
    url(r'^v1/docs', include('rest_framework_swagger.urls')),
    url(r'^v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/', include('user.urls')),
    url(r'^v1/', include('blog.urls')),
    url(r'^v1/', include('media.urls')),
)
