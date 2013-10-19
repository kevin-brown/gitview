from rest_framework import generics, response, views
from gitview.repositories.api.serializers import RepositorySerializer, \
    TreeSerializer, TreePathSerializer
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


class TreeListView(mixins.RepositoryMixin, views.APIView):

    def get(self, request, owner_name, repository_name):
        repository = Repository.objects.get()

        references = repository.git_repository.references

        serializer = TreeSerializer(references, many=True, context={
            "request": request,
            "view": self,
        })

        return response.Response(serializer.data)

class TreePathView(mixins.RepositoryMixin, mixins.TreeMixin, views.APIView):

    def get(self, request, owner_name, repository_name, tree_name,
            tree_path=None):
        repository = Repository.objects.get()

        tree = repository.git_repository.tree(tree_name)

        serializer = TreePathSerializer(instance=tree, tree_path=tree_path,
            git_repository=repository.git_repository, tree_name=tree_name,
            context={
            "request": request,
            "view": self,
        })

        return response.Response(serializer.data)
