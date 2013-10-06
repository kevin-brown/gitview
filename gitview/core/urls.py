from django.conf.urls import include, url
from django.contrib import admin
from gitview.auth.views import LoginView

admin.autodiscover()


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r"^", include("gitview.auth.urls", namespace="auth")),
    url(r"^$", LoginView.as_view(), name="index"),
)
