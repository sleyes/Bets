from django.conf.urls import url, include
from rest_framework import routers
from .views import BetsViewSet, register_bet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Bets', BetsViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register_bet/', register_bet),
    url(
        r'^api-auth/', include(
            'rest_framework.urls', namespace='rest_framework'
        )
    ),
]
