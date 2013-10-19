from django.conf.urls import include, url
from django.contrib import admin
from gitview.core.views.index import DashboardView

admin.autodiscover()


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r"^", include("gitview.auth.urls", namespace="auth")),
    url(r"^api/", include("gitview.api.urls", namespace="api")),
    url(r"^(?P<owner_name>[-\w]+)/", include("gitview.auth.profile.urls",
                                             namespace="profile")),
    url(r"^(?P<owner_name>[-\w]+)/(?P<repository_name>[-\w]+)/",
        include("gitview.repositories.urls", namespace="repos")),
    url(r"^$", DashboardView.as_view(), name="index"),
)
