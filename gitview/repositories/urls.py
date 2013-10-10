from django.conf.urls import url
from gitview.repositories import views


urlpatterns = (
    url(r"^$",
        views.TreeView.as_view(),
        name="index",
    ),
    url(r"^tree/(?P<tree_name>[-\w]+)$",
        views.TreeView.as_view(),
        name="tree_index",
    ),
    url(r"^tree/(?P<tree_name>[-\w]+)/(?P<tree_path>.+)$",
        views.TreeView.as_view(),
        name="tree_path",
    ),
    url(r"^commit/(?P<commit_hash>[\w]{7,40})$",
        views.TreeView.as_view(),
        name="commit",
    ),
    url(r"^blob/(?P<tree_name>[-\w]+)/(?P<blob_path>.+)$",
        views.BlobView.as_view(),
        name="blob",
    ),
)
