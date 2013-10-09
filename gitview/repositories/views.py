from django.views.generic import TemplateView


class CodeView(TemplateView):
    template_name = "repositories/code.html"

    def get_context_data(self, **kwargs):
        from gitview.repositories.models import Repository
        from git import Repo
        from datetime import datetime
        import os

        repository = Repository.objects.get()

        repo_dir = os.path.abspath(os.path.join(os.path.realpath(__file__),
                                                "..", "..", ".."))

        repo = Repo(repo_dir)

        repo_heads = repo.heads
        repo_branch = repo_heads.master

        kwargs["repository"] = repository
        kwargs["git_repository"] = repo

        kwargs["current_branch"] = repo_branch

        trees = []

        for tree in repo.tree().trees:
            tree_commits = repo.iter_commits(rev=repo_branch,
                                             paths=tree.abspath, max_count=1)
            tree_commit = tree_commits.next()

            tree_commit_time = datetime.fromtimestamp(
                tree_commit.committed_date
            )

            trees.append((tree, tree_commit, tree_commit_time))

        kwargs["trees"] = trees

        blobs = []

        for blob in repo.tree().blobs:
            blob_commits = repo.iter_commits(rev=repo_branch,
                                             paths=blob.abspath, max_count=1)
            blob_commit = blob_commits.next()

            blob_commit_time = datetime.fromtimestamp(
                blob_commit.committed_date
            )

            blobs.append((blob, blob_commit, blob_commit_time))

        kwargs["blobs"] = blobs

        return super(CodeView, self).get_context_data(**kwargs)


class BlobView(TemplateView):
    template_name = "repositories/blob.html"

    def get_context_data(self, **kwargs):
        from gitview.repositories.models import Repository
        from git import BadObject, Repo
        from django.http import Http404
        import os

        repository = Repository.objects.get()

        repo_dir = os.path.abspath(os.path.join(os.path.realpath(__file__),
                                                "..", "..", ".."))

        repo = Repo(repo_dir)

        kwargs["repository"] = repository
        kwargs["git_repository"] = repo

        tree_name = self.kwargs["tree_name"]

        try:
            commit = repo.commit(rev=tree_name)
        except BadObject:
            raise Http404("The commit could not be located.")

        tree = repo.tree(tree_name)

        kwargs["tree"] = tree

        blob_path = self.kwargs["blob_path"]

        try:
            blob = tree[blob_path]
        except KeyError:
            raise Http404("The blob could not be found")

        kwargs["blob"] = blob

        commit = repo.iter_commits(rev=tree_name, paths=blob_path,
                                   max_count=1).next()

        kwargs["commit"] = commit

        return super(BlobView, self).get_context_data(**kwargs)
