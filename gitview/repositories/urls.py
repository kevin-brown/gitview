from django.conf.urls import url
from gitview.repositories.commits import views as commits
from gitview.repositories.files import views as files


urlpatterns = (
    url(r"^$",
        files.TreeView.as_view(),
        name="index",
    ),
    url(r"^tree/(?P<tree_name>[-\w]+)$",
        files.TreeView.as_view(),
        name="tree_index",
    ),
    url(r"^tree/(?P<tree_name>[-\w]+)/(?P<tree_path>.+)$",
        files.TreeView.as_view(),
        name="tree_path",
    ),
    url(r"^commits/(?P<commit_hash>[\w]{7,40})$",
        files.CommitView.as_view(),
        name="commit",
    ),
    url(r"^blob/(?P<tree_name>[-\w]+)/(?P<blob_path>.+)$",
        files.BlobView.as_view(),
        name="blob",
    ),
    url(r"^commits$",
        commits.CommitListView.as_view(),
        name="commits_list",
    ),
    url(r"^commits/(?P<tree_name>[-\w]+)$",
        commits.CommitListView.as_view(),
        name="commits_list_tree",
    ),
)
