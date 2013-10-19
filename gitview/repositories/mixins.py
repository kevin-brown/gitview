class RepositoryMixin(object):

    def dispatch(self, *args, **kwargs):
        from gitview.repositories.models import Repository
        from django.http import Http404
        from git import Repo
        import os

        try:
            owner_name = kwargs["owner_name"]
            repository_name = kwargs["repository_name"]
        except KeyError:
            raise Http404("Not enough information to retrieve the repository")

        self.repository = Repository.objects.get()

        self.git_repository = self.repository.git_repository

        return super(RepositoryMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["repository"] = self.repository
        kwargs["git_repository"] = self.git_repository

        return super(RepositoryMixin, self).get_context_data(**kwargs)


class TreeMixin(object):
    default_tree = "master"

    def dispatch(self, *args, **kwargs):
        try:
            self.tree_name = kwargs["tree_name"]
        except KeyError:
            self.tree_name = self.default_tree

        self.tree = self.git_repository.tree(self.tree_name)

        return super(TreeMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        from gitview.repositories.commits.models import Commit

        kwargs["current_tree"] = self.tree
        kwargs["current_tree_name"] = self.tree_name

        if self.tree_name in self.git_repository.heads:
            kwargs["current_tree_type"] = "branch"
        elif self.tree_name in self.git_repository.tags:
            kwargs["current_tree_type"] = "tag"
        else:
            kwargs["current_tree_type"] = "tree"

        return super(TreeMixin, self).get_context_data(**kwargs)


class RepositorySection(object):

    def get_context_data(self, **kwargs):
        kwargs["active_tab"] = self.section_name

        return super(RepositorySection, self).get_context_data(**kwargs)


class FilesSectionMixin(RepositorySection):
    section_name = "files"


class CommitsSectionMixin(RepositorySection):
    section_name = "commits"


class SettingsSectionMixin(RepositorySection):
    section_name = "settings"
