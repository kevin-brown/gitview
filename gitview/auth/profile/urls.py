from django.conf.urls import url
from gitview.auth.profile import views


urlpatterns = (
    url("^$", views.IndexView.as_view(), name="index"),
)
