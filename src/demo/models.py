from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
