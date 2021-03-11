import os
import shutil
import tempfile
import requests
import pandas as pd
from demo.models import Movie, Genre, Tag
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ingest MovieLens database'

    def handle(self, *args, **options):

        if {'movies.csv', 'tags.csv'}.intersection(os.listdir('/tmp')):
            self.stdout.write(self.style.SUCCESS('using cached archive'))
            full_path = '/tmp'
        else:
            self.stdout.write(self.style.WARNING('not using cache; fetching archive'))

            # fetch movie db
            response = requests.get('https://files.grouplens.org/datasets/movielens/ml-latest-small.zip', stream=True, verify=False)
            response.raise_for_status()

            # save and unpack
            _, archive_path = tempfile.mkstemp(suffix='.zip')
            with open(archive_path, 'wb') as fd:
                for chunk in response.iter_content():
                    fd.write(chunk)
            save_path = tempfile.mkdtemp()
            shutil.unpack_archive(archive_path, save_path)
            full_path = os.path.join(save_path, 'ml-latest-small')

        # ingest - movies & genres
        df = pd.read_csv(os.path.join(full_path, 'movies.csv'))
        for _, row in df.iterrows():
            movie, was_created = Movie.objects.get_or_create(
                movie_id=row['movieId'],
                defaults=dict(
                    name=row['title'],
                )
            )
            genre_names = row['genres'].split('|')
            genres = [Genre.objects.get_or_create(name=genre)[0] for genre in genre_names]
            movie.genres.set(genres)

        # ingest - tags
        df = pd.read_csv(os.path.join(full_path, 'tags.csv'))
        for _, row in df.iterrows():
            # get matching movie
            try:
                movie = Movie.objects.get(movie_id=row['movieId'])
            except Movie.DoesNotExist:
                self.stdout.write(self.style.WARNING('movieId {} does not exist referenced in tags.csv'.format(row['movieId'])))
                continue
            # add tag
            tag, _ = Tag.objects.get_or_create(name=row['tag'])
            movie.tags.add(tag)
