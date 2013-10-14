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

    is_public = models.BooleanField(default=True)

    has_issues = models.BooleanField(default=True)

    objects = RepositoryManager()

    class Meta:
        verbose_name_plural = "repositories"

    def __unicode__(self):
        return "%s/%s" % (self.owner.username, self.name)

    @property
    def git_repository(self):
        from git import Repo

        return Repo(self.repository_location)

    @property
    def repository_location(self):
        return "/home/git/repositories/%s" % self.location

    def create_git_repository(self):
        from git import Repo

        Repo.init(self.repository_location, bare=True)

    def save(self, *args, **kwargs):
        if not self.location:
            folder_path = "%s/%s.git" % (self.owner.username, self.name)

            self.location = folder_path

            self.create_git_repository()

        return super(Repository, self).save(*args, **kwargs)
