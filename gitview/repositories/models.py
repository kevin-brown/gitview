from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType


class Repository(models.Model):
    owner_id = models.PositiveIntegerField()
    owner_ct = models.ForeignKey(ContentType)

    owner = generic.GenericForeignKey(fk_field="owner_id",
                                       ct_field="owner_ct")

    name = models.SlugField(max_length=50, unique=True)


class Commit(models.Model):
    sha_hash = models.CharField(max_length=40)

    repository = models.ForeignKey("repositories.Repository",
                                   related_name="commits")