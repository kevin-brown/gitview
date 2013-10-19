from rest_framework import fields as rest_fields, serializers
from gitview.repositories.models import Repository
from gitview.repositories.api import fields as api_fields


class RepositorySerializer(serializers.ModelSerializer):
    default_branch_url = api_fields.RepositoryTreeField(
        source="default_branch")

    class Meta:
        fields = ("id", "name", "default_branch", "default_branch_url",
                  "is_public", "has_issues", )
        read_only_fields = ("id", "name", )

        model = Repository


class TreeSerializer(serializers.Serializer):
    name = rest_fields.CharField()
    url = api_fields.RepositoryTreeField(source="name")


class TreePathSerializer(serializers.Serializer):

    def __init__(self, git_repository, tree_name, tree_path=None,
                 *args, **kwargs):
        self.git_repository = git_repository
        self.tree_name = tree_name
        self.tree_path = tree_path

        super(TreePathSerializer, self).__init__(*args, **kwargs)

    def to_native(self, obj):
        from git import Blob, Tree

        data = {
            "name": obj.name,
            "path": obj.path,
        }

        obj_commits = self.git_repository.iter_commits(rev=self.tree_name,
                                                       paths=obj.path,
                                                       max_count=1)

        data["commit_hash"] = obj_commits.next().hexsha

        if isinstance(obj, Blob):
            pass
        elif isinstance(obj, Tree):
            pass

        return data
