from django.conf.urls import include, url
from django.contrib import admin
from gitview.core.views.index import DashboardView

admin.autodiscover()


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r"^api/", include("gitview.api.urls", namespace="api")),
)
