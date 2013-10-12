from django.views.generic import ListView, TemplateView, View
from gitview.repositories import mixins
from gitview.repositories.commits import CommitPaginator


class CommitListView(mixins.RepositoryMixin, mixins.TreeMixin,
                     mixins.CommitsSectionMixin, ListView):
    context_object_name = "commits"
    paginate_by = 25
    paginator_class = CommitPaginator
    template_name = "repositories/commits.html"

    def get_queryset(self):
        from gitview.repositories.commits.models import Commit

        commits = self.git_repository.iter_commits(rev=self.tree_name)

        return [Commit(commit, self.repository) for commit in commits]


class CommitView(mixins.RepositoryMixin, mixins.CommitsSectionMixin,
                 TemplateView):
    template_name = "repositories/commit.html"

    def get_context_data(self, **kwargs):
        from django.http import Http404
        from git import BadObject
        from gitview.repositories.commits.models import Commit

        commit_hash = self.kwargs["commit_hash"]
        commit = Commit(self.git_repository.commit(commit_hash))

        kwargs["commit"] = commit

        try:
            previous_commit = self.git_repository.commit("%s~1" % commit_hash)
            diff = previous_commit.diff(commit.commit, create_patch=True)
        except BadObject:
            raise Http404("We can't get the diff for this commit")

        kwargs["commit_diff"] = diff

        return super(CommitView, self).get_context_data(**kwargs)


class DiffView(mixins.RepositoryMixin, View):
    def get(self, *args, **kwargs):
        from django.http import HttpResponse
        from git import BadObject

        commit_hash = self.kwargs["commit_hash"]
        commit = self.git_repository.commit(commit_hash)

        patch = self.git_repository.git.execute(["git", "diff",
                    "%s^!" % commit.hexsha])

        return HttpResponse(patch, content_type="text/plain; charset=utf-8")


class PatchView(mixins.RepositoryMixin, View):
    def get(self, *args, **kwargs):
        from django.http import HttpResponse
        from git import BadObject

        commit_hash = self.kwargs["commit_hash"]
        commit = self.git_repository.commit(commit_hash)

        patch = self.git_repository.git.execute(["git", "format-patch",
                    "%s^!" % commit.hexsha, "--stdout"])

        return HttpResponse(patch, content_type="text/plain; charset=utf-8")
