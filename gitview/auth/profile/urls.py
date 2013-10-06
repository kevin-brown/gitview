from django.conf.urls import url


urlpatterns = (
    url("^$", "django.contrib.auth.views.login", name="index"),
)
