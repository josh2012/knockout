from django.conf.urls import patterns, url

urlpatterns = patterns('content',
    url('^$', 'views.index', name='index'),
)