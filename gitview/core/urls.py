from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r"^", include("gitview.auth.urls", namespace="auth")),
    url(r"^logout/$", "django.contrib.auth.views.logout",
        name="logout"),
    url(r"^$", "django.contrib.auth.views.login", name="index"),
)
