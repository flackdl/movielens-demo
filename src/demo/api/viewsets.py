from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.gzip import gzip_page
from rest_framework import viewsets

from demo.api.filters import MovieFilter
from demo.api.serializers import MovieSerializer, GenreSerializer, TagSerializer
from demo.models import Movie, Genre, Tag

CACHE_DAY = 3600 * 24


@method_decorator(gzip_page, name='dispatch')
@method_decorator(cache_page(timeout=CACHE_DAY), name='dispatch')
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_class = MovieFilter
    search_fields = ['name']


@method_decorator(gzip_page, name='dispatch')
@method_decorator(cache_page(timeout=CACHE_DAY), name='dispatch')
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filterset_fields = ('name',)


@method_decorator(gzip_page, name='dispatch')
@method_decorator(cache_page(timeout=CACHE_DAY), name='dispatch')
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_fields = ('name',)
    pagination_class = None
