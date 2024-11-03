from rest_framework import routers
from .views import UserViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')

urlpatterns = [*router.urls,]