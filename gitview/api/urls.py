from django.conf.urls import include, url
from gitview.api import views


urlpatterns = (
    url("^$", views.IndexView.as_view(), name="index"),
    url("^repositories/", include("gitview.repositories.api.urls")),
)
