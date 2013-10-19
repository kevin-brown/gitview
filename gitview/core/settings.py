import os

AUTH_USER_MODEL = "auth.User"

DEBUG = True

# The secret key should be set through the environment variable
# "DJANGO_SECRET_KEY".  The default is only here for quick testing and should
# not be used in a production environment.

SECRET_KEY = os.environ.get("GITVIEW_SECRET_KEY",
                            "43VZ9xksRQS`z+_}2Ac^c3!$3_Wl!"
                            "AL{ysyh03<p|I%39YE4qf23dZp9Xd")

INSTALLED_APPS = (
    "gitview.core",
    "gitview.auth",
    "gitview.repositories",
    "gitview.issues",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "south",
    "rest_framework",
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
    "gitview.core.context_processors.settings",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("GITVIEW_DATABASE_NAME", "devdb"),
        'USER': 'postgres',
        'PASSWORD': os.environ.get("GITVIEW_DATABASE_PASSWORD", "dev"),
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

ROOT_URLCONF = "gitview.core.urls"

TIME_ZONE = "America/New_York"

DATETIME_FORMAT = "Y-m-d H:i:s"

STATIC_URL = "/static/"

LOGIN_URL = "auth:login"

LOGIN_REDIRECT_URL = "index"
