FROM python:3.8-buster
ADD src /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mkdir -p static-assets
RUN python manage.py collectstatic --no-input
ENTRYPOINT /app/docker-entrypoint.sh
