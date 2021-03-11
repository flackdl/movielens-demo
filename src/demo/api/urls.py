from django.urls import include, path
from rest_framework import routers
from demo.api import viewsets

router = routers.DefaultRouter()
router.register('movie', viewsets.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
