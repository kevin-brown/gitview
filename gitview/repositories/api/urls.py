from django.conf.urls import url
from gitview.repositories import COMMIT_REGEX, REPOSITORY_REGEX, TREE_REGEX, \
    TREE_PATH_REGEX
from gitview.repositories.api import views


urlpatterns = (
    url(
        r"^%s$" % REPOSITORY_REGEX,
        views.RepositoryView.as_view(),
        name="index",
    ),
    url(
        r"^%s/commits/%s" % (REPOSITORY_REGEX, COMMIT_REGEX),
        views.CommitDetailView.as_view(),
        name="commit",
    ),
    url(
        r"^%s/commits/%s" % (REPOSITORY_REGEX, TREE_REGEX),
        views.CommitListView.as_view(),
        name="commit_list",
    ),
    url(
        r"^%s/trees$" % REPOSITORY_REGEX,
        views.TreeListView.as_view(),
        name="tree_list",
    ),
    url(
        r"%s/trees/%s$" % (REPOSITORY_REGEX, TREE_REGEX),
        views.TreePathView.as_view(),
        name="tree_index",
    ),
    url(
        r"%s/trees/%s/%s$" % (REPOSITORY_REGEX, TREE_REGEX, TREE_PATH_REGEX),
        views.TreePathView.as_view(),
        name="tree_path",
    ),
)
