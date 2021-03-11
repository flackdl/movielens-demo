from django.contrib import admin
from demo.models import Movie, Genre, Tag


@admin.register(Movie, Genre, Tag)
class Admin(admin.ModelAdmin):
    pass
