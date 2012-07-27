""" Common Project Settings """

# Website Settings
SITE = {
    'domain': 'aboutme.com',
    'name': 'AboutMe',
    'tagline': 'It\'s all about you !',
}

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/user/%s/" % u.username,
}

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sampleprojectemail@gmail.com'
EMAIL_HOST_PASSWORD = 'SAMPLEPROJECT'
EMAIL_PORT = 587

# Django Registration
from django.core.urlresolvers import reverse_lazy
ACCOUNT_ACTIVATION_DAYS = 2
REGISTRATION_OPEN = True
LOGIN_REDIRECT_URL = reverse_lazy('index')

# Users
AUTH_PROFILE_MODULE = "users.UserProfile"
