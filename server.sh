#!/bin/bash
cd /Ex_finder_server/Ex_project/project/backend
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000