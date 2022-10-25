#!/bin/bash
cd /Ex_finder_server/Ex_project/project/backend
python3 manage.py makemigrations
python3 manage.py migrate
if [ $ENV_TYPE = "service" ]
then
    python3 manage.py runserver 0.0.0.0:8000
fi