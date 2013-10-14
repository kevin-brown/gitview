from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from gitview.repositories.managers import RepositoryManager


class Repository(models.Model):
    owner_id = models.PositiveIntegerField()
    owner_ct = models.ForeignKey(ContentType)

    owner = generic.GenericForeignKey(fk_field="owner_id",
                                       ct_field="owner_ct")

    name = models.SlugField(max_length=50, unique=True)

    location = models.FilePathField(path="/home/git/repositories/",
                                    allow_files=False, allow_folders=True,
                                    recursive=True, match=".*\.git")

    objects = RepositoryManager()

    class Meta:
        verbose_name_plural = "repositories"
