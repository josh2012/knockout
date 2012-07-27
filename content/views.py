"""Content Views"""

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response


template = lambda name: 'content/%s' % name

def index(request):
    if request.user.is_authenticated():
        HttpResponseRedirect(reverse('user_home', kwargs={'username': request.user.username}))
    return render_to_response(template('index.html'), RequestContext(request))
