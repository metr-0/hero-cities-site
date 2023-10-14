#!/bin/sh

echo "Running database migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "creating superuser"
python3 manage.py initadmin

exec "$@"