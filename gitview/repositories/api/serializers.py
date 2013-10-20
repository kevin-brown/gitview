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


class CommitSerializer(serializers.Serializer):
    hash = rest_fields.CharField(source="hexsha")
    short_hash = rest_fields.CharField(source="shorthash")

    summary = rest_fields.CharField()
    description = rest_fields.CharField()

    committed_time = rest_fields.DateTimeField()


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
        from django.core.urlresolvers import reverse

        data = {
            "name": obj.name,
            "path": obj.path,
        }

        obj_commits = self.git_repository.iter_commits(rev=self.tree_name,
                                                       paths=obj.path,
                                                       max_count=1)

        data["commit_hash"] = obj_commits.next().hexsha

        if isinstance(obj, Blob):
            data["type"] = "blob"

            data["gitview_blob_url"] = "blob/%s/%s" % (self.tree_name,
                                                       obj.path)
        elif isinstance(obj, Tree):
            data["type"] = "tree"

            data["gitview_tree_url"] = "tree/%s/%s" % (self.tree_name,
                                                       obj.path)

        return data

    @property
    def data(self):
        data = super(TreePathSerializer, self).data

        trees = [obj for obj in data if obj["type"] == "tree"]
        blobs = [obj for obj in data if obj["type"] == "blob"]

        commit = self.git_repository.iter_commits(rev=self.tree_name,
                                                  paths=self.tree_path,
                                                  max_count=1).next()

        return {
            "commit_hash": commit.hexsha,
            "trees": trees,
            "blobs": blobs,
            "path": self.tree_path,
        }
