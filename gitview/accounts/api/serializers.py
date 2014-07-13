from rest_framework import serializers
from gitview.accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
