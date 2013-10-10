from django.views.generic import TemplateView
from gitview.repositories import mixins


class TreeView(mixins.RepositoryMixin, mixins.TreeMixin,
               mixins.FilesSectionMixin, TemplateView):
    template_name = "repositories/tree.html"

    def get_context_data(self, **kwargs):
        from datetime import datetime

        try:
            tree_path = self.kwargs["tree_path"]
        except KeyError:
            tree_path = self.tree.path

        if tree_path:
            self.tree = self.tree[tree_path]

        repo_heads = self.git_repository.heads

        kwargs["commit"] = self.git_repository.commit(self.tree_name)

        trees = []

        for tree in self.tree.trees:
            tree_commits = self.git_repository.iter_commits(
                rev=self.tree_name, paths=tree.abspath, max_count=1)
            tree_commit = tree_commits.next()

            tree_commit_time = datetime.fromtimestamp(
                tree_commit.committed_date
            )

            trees.append((tree, tree_commit, tree_commit_time))

        kwargs["trees"] = trees

        blobs = []

        for blob in self.tree.blobs:
            blob_commits = self.git_repository.iter_commits(
                rev=self.tree_name, paths=blob.abspath, max_count=1)
            blob_commit = blob_commits.next()

            blob_commit_time = datetime.fromtimestamp(
                blob_commit.committed_date
            )

            blobs.append((blob, blob_commit, blob_commit_time))

        kwargs["blobs"] = blobs

        return super(TreeView, self).get_context_data(**kwargs)


class BlobView(mixins.RepositoryMixin, mixins.TreeMixin,
               mixins.FilesSectionMixin, TemplateView):
    template_name = "repositories/blob.html"

    def get_context_data(self, **kwargs):
        from git import BadObject
        from django.http import Http404

        try:
            commit = self.git_repository.commit(rev=self.tree_name)
        except BadObject:
            raise Http404("The commit could not be located.")

        blob_path = self.kwargs["blob_path"]

        try:
            blob = self.tree[blob_path]
        except KeyError:
            raise Http404("The blob could not be found")

        kwargs["blob"] = blob

        commit = self.git_repository.iter_commits(rev=self.tree_name,
                                                  paths=blob_path,
                                                  max_count=1).next()

        kwargs["commit"] = commit

        return super(BlobView, self).get_context_data(**kwargs)


class CommitView(mixins.RepositoryMixin, mixins.FilesSectionMixin,
                 TemplateView):
    template_name = "repositories/commit.html"

    def get_context_data(self, **kwargs):
        commit_hash = self.kwargs["commit_hash"]
        commit = self.git_repository.commit(commit_hash)

        kwargs["commit"] = commit

        diff = commit.diff("%s~1" % commit_hash, create_patch=True)

        kwargs["commit_diff"] = diff

        return super(CommitView, self).get_context_data(**kwargs)
