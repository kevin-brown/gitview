class RepositoryMixin(object):

    def dispatch(self, *args, **kwargs):
        from gitview.repositories.models import Repository
        from django.http import Http404
        from git import Repo
        import os

        try:
            owner_name = self.kwargs["owner_name"]
            repository_name = self.kwargs["repository_name"]
        except KeyError:
            raise Http404("Not enough information to retrieve the repository")

        self.repository = Repository.objects.get()

        repo_dir = os.path.abspath(os.path.join(os.path.realpath(__file__),
                                                "..", "..", ".."))
        self.git_repository = Repo(repo_dir)

        return super(RepositoryMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["repository"] = self.repository
        kwargs["git_repository"] = self.git_repository

        return super(RepositoryMixin, self).get_context_data(**kwargs)


class TreeMixin(object):
    default_tree = "master"

    def dispatch(self, *args, **kwargs):
        try:
            self.tree_name = self.kwargs["tree_name"]
        except KeyError:
            self.tree_name = self.default_tree

        self.tree = self.git_repository.tree(self.tree_name)

        return super(TreeMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["current_tree"] = self.tree
        kwargs["current_tree_name"] = self.tree_name

        return super(TreeMixin, self).get_context_data(**kwargs)


class RepositorySection(object):

    def get_context_data(self, **kwargs):
        kwargs["active_tab"] = self.section_name

        return super(RepositorySection, self).get_context_data(**kwargs)


class FilesSectionMixin(RepositorySection):
    section_name = "files"
