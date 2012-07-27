""" Local settings """

import os
from . import PROJECT_DIR

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Yugal Jindle', 'yugal.jindle@joshlabs.in'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'aboutme.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Kolkata'
