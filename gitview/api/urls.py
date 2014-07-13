from django.conf.urls import include, url
from rest_framework import routers
from gitview.accounts.api.views import UserViewSet

router = routers.DefaultRouter()

router.register("users", UserViewSet)

urlpatterns = router.urls
