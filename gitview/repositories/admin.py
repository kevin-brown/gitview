from django.contrib import admin
from gitview.repositories.models import Repository


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", )

admin.site.register(Repository, RepositoryAdmin)
