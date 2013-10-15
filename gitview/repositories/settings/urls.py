from django.conf.urls import url
from gitview.repositories.settings import views


urlpatterns = (
    url("^$", views.SettingsView.as_view(), name="index"),
)
