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
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "south",
    "rest_framework",
    "pipeline",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
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
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("GITVIEW_DATABASE_NAME", "../gitview.db"),
        "USER": os.environ.get("GITVIEW_DATABASE_USER", ""),
        "PASSWORD": os.environ.get("GITVIEW_DATABASE_PASSWORD", ""),
        "HOST": os.environ.get("GITVIEW_DATABASE_HOST", "localhost"),
        "PORT": os.environ.get("GITVIEW_DATABASE_PORT", ""),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

STATICFILES_FINDERS = (
    'pipeline.finders.PipelineFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

PIPELINE_DISABLE_WRAPPER = True

PIPELINE_COMPILERS = (
    "pipeline_compass.compiler.CompassCompiler",
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_CSS = {
    "bootstrap": {
        "source_filenames": (
            "css/font-awesome.css",
            "css/bootstrap.css",
            ),
        "output_filename": "css/bootstrap.css",
        },
    "repositories": {
        "source_filenames": (
            "css/repositories/core.scss",
            ),
        "output_filename": "css/repositories.css",
        },
    }

PIPELINE_JS_COMPRESSOR = None#'pipeline.compressors.yui.YUICompressor'

PIPELINE_JS = {
    "angular": {
        "source_filenames": (
            "js/angular/app.js",
            "js/angular/timeago.js",
        ),
        "output_filename": "js/angular.js",
    },
    "jquery": {
        "source_filenames": (
            "js/jquery.js",
            "js/timeago.js",
        ),
        "output_filename": "js/jquery.js",
    },
    "core": {
        "source_filenames": (
            "js/bootstrap.js",
            "js/handlebars.js",
            "js/ember.js",
            "js/ember-data.js",
            "js/ember/bootstrap/core.js",
            "js/ember/bootstrap/button.js",
            "js/ember/bootstrap/notifications.js",
            "js/ember/app.js",
            "js/core.templates.js",
            "js/ember/router.js",
            "js/ember/models/repository.js",
            "js/ember/controllers/repository.js",
        ),
        "output_filename": "js/core.js",
    },
    "auth": {
        "source_filenames": (
            "js/auth.templates.js",
            "js/views/login.js",
        ),
        "output_filename": "js/auth.js",
    },
    "repositories": {
        "source_filenames": (
            "js/angular/repositories/controllers.js",
            "js/angular/repositories/directives.js",
            "js/angular/repositories/services.js",
        ),
        "output_filename": "js/repositories.js",
    },
}

ALLOWED_HOSTS = (
    "localhost",
    os.environ.get("DJANGO_HOST", None),
)

ROOT_URLCONF = "gitview.core.urls"

TIME_ZONE = "America/New_York"

DATETIME_FORMAT = "Y-m-d H:i:s"

STATIC_URL = "/static/"

STATIC_ROOT = "static/"

LOGIN_URL = "auth:login"

LOGIN_REDIRECT_URL = "index"
