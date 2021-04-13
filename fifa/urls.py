from django.urls import include, path
from rest_framework import routers

from fifa.views import ClubViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register('clubs', ClubViewSet)
router.register('players', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]