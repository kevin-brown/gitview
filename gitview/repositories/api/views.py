from rest_framework import generics, response, views
from gitview.repositories.api.serializers import RepositorySerializer, \
    CommitSerializer, TreeSerializer, TreePathSerializer
from gitview.repositories.models import Repository
from gitview.repositories import mixins


class RepositoryView(mixins.RepositoryMixin, generics.RetrieveUpdateAPIView):
    serializer_class = RepositorySerializer
    model = Repository

    gitview_base_url = "repositories"
    gitview_format_url = "repositories/%(owner)s/%(name)s"

    def get_object(self, queryset=None):
        obj = self.repository

        self.check_object_permissions(self.request, obj)

        return obj

    def get_queryset(self):
        return Repository.objects.all()


class CommitListView(mixins.RepositoryMixin, mixins.TreeMixin, views.APIView):

    def get(self, *args, **kwargs):
        from gitview.repositories.commits.models import Commit

        commits = self.git_repository.iter_commits(rev=self.tree_name)

        commits = [Commit(commit, self.repository) for commit in commits]

        commits_day_data = {}

        for commit in commits:
            date = commit.committed_time.date()

            if not date in commits_day_data:
                commits_day_data[date] = []

            commits_day_data[date].append(commit)

        commits_list = []

        for commit in commits:
            date = commit.committed_time.date()

            if not date in commits_day_data:
                continue

            commits_list.append({
                    "date": date,
                    "commits": commits_day_data[date],
            })

            del commits_day_data[date]

        commits = []

        for day in commits_list:
            commits_day = []

            for commit in day["commits"]:
                commits_day.append(CommitSerializer(commit).data)

            print commits_day

            commits.append({
                    "date": day["date"],
                    "commits": commits_day,
            })

        return response.Response(commits)


class CommitDetailView(mixins.RepositoryMixin, views.APIView):

    def get(self, request, owner_name, repository_name, commit_hash):
        from django.views.decorators.http import condition

        def commit_etag(request):
            from gitview.repositories.commits.models import Commit

            commit = Commit(self.git_repository.commit(commit_hash))

            return commit.hexsha

        def commit_modified(request):
            from gitview.repositories.commits.models import Commit

            commit = Commit(self.git_repository.commit(commit_hash))

            return commit.committed_time

        @condition(etag_func=commit_etag, last_modified_func=commit_modified)
        def cached_view(request):
            from gitview.repositories.commits.models import Commit

            commit = Commit(self.git_repository.commit(commit_hash))

            serializer = CommitSerializer(commit)

            return response.Response(serializer.data)

        return cached_view(request)

class TreeListView(mixins.RepositoryMixin, views.APIView):

    def get(self, request, owner_name, repository_name):
        references = self.repository.git_repository.references

        serializer = TreeSerializer(references, many=True, context={
            "request": request,
            "view": self,
        })

        return response.Response(serializer.data)

class TreePathView(mixins.RepositoryMixin, mixins.TreeMixin, views.APIView):

    def get(self, request, owner_name, repository_name, tree_name,
            tree_path=None):
        tree = self.repository.git_repository.tree(tree_name)

        if tree_path:
            tree = tree[tree_path]

        serializer = TreePathSerializer(instance=tree, tree_path=tree_path,
            git_repository=self.git_repository, tree_name=tree_name,
            context={
            "request": request,
            "view": self,
        }, many=True)

        return response.Response(serializer.data)
