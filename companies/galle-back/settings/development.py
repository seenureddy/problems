import os
import dj_database_url
from .common import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG =  True

ALLOWED_HOSTS = []

# # Database
# # https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
    	env="DATABASE_URL"	,
    	default='sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))
}
