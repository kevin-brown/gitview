from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as DjangoUser, \
    Group as DjangoGroup
from gitview.auth.models import User


class UserAdmin(UserAdmin):
    pass

# Unregister the old `django.contrib.auth` models that should not have been
# registered in the first place.

admin.site.unregister(DjangoUser)
admin.site.unregister(DjangoGroup)

# Register the GitView models

admin.site.register(User, UserAdmin)
