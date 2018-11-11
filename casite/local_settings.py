# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&t1qb9co$7c51k9(=y_qdjidjsidjsduihnjase6qs-7z0+)sfr2q#^(q6na='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['139.59.8.171','caandcs.com','www.caandcs.com']
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_prod',
        'USER': 'dbadmin',
        'PASSWORD':'jhadiwala123#',
        'HOST' : 'localhost',

    }
}

