#!/bin/bash
rm -rf uncraftedapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations uncraftedapi
python3 manage.py migrate uncraftedapi
python manage.py loaddata user
python manage.py loaddata post
python manage.py loaddata trade
python manage.py loaddata message
python manage.py loaddata trademessage
