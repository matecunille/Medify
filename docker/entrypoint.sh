#!/bin/bash
set -e

mkdir -p /usr/local/app/media
mkdir -p /usr/local/app/staticfiles
chmod -p 777 /usr/local/app/media || true
chmod -p 777 /usr/local/app/staticfiles || true

python manage.py makemigrations users
python manage.py makemigrations consultations
python manage.py migrate --noinput
python manage.py loaddata initial_specialties
python manage.py collectstatic --no-input --clear || true

exec gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application