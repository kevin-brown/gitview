from rest_framework import fields
from rest_framework.reverse import reverse


class RepositoryTreeField(fields.Field):

    def to_native(self, default_branch):
        request = self.context["request"]
        view = self.context["view"]

        url_kwargs = view.kwargs
        url_kwargs["tree_name"] = default_branch

        url = reverse("api:tree_index", kwargs=url_kwargs, request=request)

        return url
