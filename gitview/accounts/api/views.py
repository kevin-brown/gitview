from rest_framework import viewsets
from gitview.accounts.models import User


class UserViewSet(viewsets.ModelViewSet):
    model = User
