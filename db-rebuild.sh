#!/usr/bin/env bash

echo "DELETING FACTORY SIMULATOR DATABASE"
PGPASSWORD="${DB_USER_PG_PASSWORD}" dropdb -w -h localhost -U "${DB_USER}" factory_simulator
echo "CREATING FACTORY SIMULATOR DATABASE"
PGPASSWORD="${DB_USER_PG_PASSWORD}" createdb -w -h localhost -U "${DB_USER}" factory_simulator

echo "MIGRATING FACTORY SIMULATOR DATABASE"
python manage.py makemigrations
python manage.py migrate
