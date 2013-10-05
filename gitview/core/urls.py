from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
        name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout",
        name="logout"),
)
