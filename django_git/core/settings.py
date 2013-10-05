import os

AUTH_USER_MODEL = "auth.User"

DEBUG = True

# The secret key should be set through the environment variable
# "DJANGO_SECRET_KEY".  The default is only here for quick testing and should
# not be used in a production environment.

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY",
                            "43VZ9xksRQS`z+_}2Ac^c3!$3_Wl!"
                            "AL{ysyh03<p|I%39YE4qf23dZp9Xd")

INSTALLED_APPS = (
    "django_git.auth",
    "django_git.repositories",
    "django_git.issues",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DJANGO_DATABASE_NAME", "devdb"),
        'USER': 'postgres',
        'PASSWORD': os.environ.get("DJANGO_DATABASE_PASSWORD", "dev"),
        "HOST": "localhost",
        "PORT": "",
        "OPTIONS": {
            "connect_timeout": 15,
        },
    }
}

ALLOWED_HOSTS = (
    "localhost",
    os.environ.get("DJANGO_HOST", None),
)

ROOT_URLCONF = "django_git.core.urls"

STATIC_URL = "/static/"