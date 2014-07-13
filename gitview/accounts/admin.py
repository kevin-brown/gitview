from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gitview.accounts.models import User


class UserAdmin(UserAdmin):
    pass

# Register the GitView models

admin.site.register(User, UserAdmin)
