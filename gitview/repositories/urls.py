from django.conf.urls import url
from gitview.repositories import views


urlpatterns = (
    url(r"^$",
        views.CodeView.as_view(),
        name="index",
    ),
    url(r"^blob/(?P<tree_name>[-\w]+)/(?P<blob_path>.+)$",
        views.BlobView.as_view(),
        name="blob",
    ),
)
