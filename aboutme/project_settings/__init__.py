""" Aggregates all types of settings to settings.py """

import os
PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

from django_settings import *
from common_settings import *
from local_settings import *
