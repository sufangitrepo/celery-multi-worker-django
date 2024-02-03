#!/bin/sh

echo "Start migration"

python manage.py migrate

echo "End migration"

exec "$@"
