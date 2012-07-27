from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ## Custom apps
    url(r'', include('content.urls')),
    url(r'users/', include('users.urls')),
    ## Other apps
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
