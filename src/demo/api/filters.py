from django_filters import rest_framework as filters

from demo.models import Movie


class MovieFilter(filters.FilterSet):

    class Meta:
        model = Movie
        fields = {
            'name': ['exact'],
            'genres': ['exact'],
            'tags': ['exact'],
        }
