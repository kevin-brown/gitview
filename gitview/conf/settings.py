import os

AUTH_USER_MODEL = "accounts.User"

DEBUG = os.environ.get("DEBUG", False)

SECRET_KEY = os.environ.get("GITVIEW_SECRET_KEY")

INSTALLED_APPS = (
    "gitview.accounts",
    "gitview.core",
    "gitview.issues",
    "gitview.repositories",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "pipeline",
    "rest_framework",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pipeline.middleware.MinifyHTMLMiddleware",
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
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME", "gitview"),
        "USER": os.environ.get("DB_USER", "gitview"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_PORT_5432_TCP_ADDR", "localhost"),
        "PORT": os.environ.get("DB_PORT_5432_TCP_PORT", "5432"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

STATICFILES_FINDERS = (
    "pipeline.finders.PipelineFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

PIPELINE_DISABLE_WRAPPER = True

PIPELINE_COMPILERS = (
    "pipeline_compass.compiler.CompassCompiler",
)

PIPELINE_CSS_COMPRESSOR = "pipeline.compressors.yui.YUICompressor"

PIPELINE_CSS = {}

PIPELINE_JS_COMPRESSOR = None

PIPELINE_JS = {}

ALLOWED_HOSTS = (
    os.environ.get("DJANGO_HOST", "localhost"),
)

ROOT_URLCONF = "gitview.conf.urls"

TIME_ZONE = "America/New_York"

DATETIME_FORMAT = "Y-m-d H:i:s"

STATIC_URL = "/static/"

STATIC_ROOT = "static/"

LOGIN_URL = "auth:login"

LOGIN_REDIRECT_URL = "index"
