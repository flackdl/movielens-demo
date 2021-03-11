from django.urls import include, path
from rest_framework import routers
from demo.api import viewsets

router = routers.DefaultRouter()
router.register('movie', viewsets.MovieViewSet)
router.register('genre', viewsets.GenreViewSet)
router.register('tag', viewsets.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
