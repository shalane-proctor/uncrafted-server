#!/bin/bash
rm -rf uncraftedapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations uncraftedapi
python3 manage.py migrate uncraftedapi
