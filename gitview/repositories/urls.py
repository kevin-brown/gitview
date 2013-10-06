from django.conf.urls import url
from gitview.repositories import views


urlpatterns = (
    url(r"^$",
        views.CodeView.as_view(),
        name="index",
    ),
)
