from django.conf import settings

def site_context(request):
    return {'site': settings.SITE}
