from django.conf.urls import url


urlpatterns = (
    url(r"^$",
        "django.contrib.auth.views.login",
        name="index",
    ),
)
