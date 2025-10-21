#!/usr/bin/env bash

# Create media directory and set permissions
mkdir -p media
chmod 755 media

python manage.py makemigrations users
python manage.py makemigrations consultations
python manage.py migrate --noinput
python manage.py loaddata initial_specialties
python manage.py collectstatic --noinput
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application