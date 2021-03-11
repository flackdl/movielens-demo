from rest_framework import serializers
from demo.models import Movie, Genre, Tag


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
