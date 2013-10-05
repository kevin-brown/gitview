import os

AUTH_USER_MODEL = "auth.User"

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
    "django.contrib.contenttypes",
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
