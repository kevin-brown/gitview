from django.views.generic import ListView
from gitview.repositories import mixins


class CommitListView(mixins.RepositoryMixin, mixins.TreeMixin,
                     mixins.CommitsSectionMixin, ListView):
    context_object_name = "commits"
    paginate_by = 25
    template_name = "repositories/commits.html"

    def get_queryset(self):
        from gitview.repositories.commits.models import Commit

        commits = self.git_repository.iter_commits(rev=self.tree_name)

        return [Commit(commit, self.repository) for commit in commits]
