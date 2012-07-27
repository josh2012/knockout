from django.conf.urls import patterns, url

urlpatterns = patterns('users',
    url('^ajax/info', 'views.ajax', name='ajax'),
    url('^(?P<username>\w+)', 'views.user_home', name='user_home'),
)