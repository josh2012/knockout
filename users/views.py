import json
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

template = lambda name: 'users/%s' % name

@login_required
def user_home(request, username):
    return render_to_response(template('user_home.html'), RequestContext(request))

@login_required
@csrf_exempt
def ajax(request):
    if request.method == 'GET':
        tab = request.GET.get('tab')
        data = dict()
        if tab.lower() == 'profile':
            data['tab'] = 'Profile'
            data['fname'] = request.user.first_name
            data['lname'] = request.user.last_name
            data['email'] = request.user.email
        return HttpResponse(json.dumps(data), content_type='application/json')
    elif request.method == 'POST':
        data = request.POST
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        user = request.user
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()
        return HttpResponse()
