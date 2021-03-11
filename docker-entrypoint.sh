python manage.py migrate
gunicorn movielens_demo.wsgi:application -b :8080
