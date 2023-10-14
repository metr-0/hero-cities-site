#!/bin/sh

echo "Running database migrations"
python3 manage.py migrate

exec "$@"
