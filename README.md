# MovieLens demo

This is a simple web app that demonstrates ingesting the (MovieLens dataset)[https://grouplens.org/datasets/movielens/latest/]
and presenting the results in a friendly UI that can search and filter by titles, genres, and tags.

## Building

This app is build with Python 3, Django 3, Vue, and Bulma.  The default database is sqlite but you can easily swap in PostgreSQL to make use of it's [Full Text Search](https://www.postgresql.org/docs/9.5/textsearch.html).

Create a python virtual environment:

    python3 -mvenv ~/.envs/movielens
    . ~/.envs/movielens/bin/activate

Install requirements:
    
    pip install -r src/requirements.txt

Initialize django app:

    python src/manage.py migrate

Ingest MovieLens dataset:

*This takes a few minutes.*

    python src/manage.py ingest

Run web server:

    python src/manage.py runserver localhost:8080

App will be running at http://localhost:8080

API: http://localhost:8080/api

Admin: http://localhost:8080/admin (run `python src/manage.py createsuperuser` first)
