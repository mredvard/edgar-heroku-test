from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heroku_test.views.home', name='home'),
    # url(r'^heroku_test/', include('heroku_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/admin(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.DJANGO_ROOT + "/contrib/admin/static/admin/",
                            }),
)
