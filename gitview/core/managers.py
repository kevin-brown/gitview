from django.db import models


class BaseManager(models.Manager):

    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)
