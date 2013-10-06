from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet
from gitview.core.managers import BaseManager


class RepositoryManager(BaseManager):

    def get_query_set(self):
        return RepositoryQuerySet(self.model)


class RepositoryQuerySet(QuerySet):

    def filter_for_user(self, user):
        ct = ContentType.objects.get_for_model(user)

        return self.filter(owner_id=user.id, owner_ct=ct)
