#!/bin/bash
set -e

mkdir -p /usr/local/app/staticfiles /usr/local/app/media

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate --no-input

exec "$@"
