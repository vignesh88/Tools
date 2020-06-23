#!/bin/bash

python tools/start.py
python tools/manage.py makemigrations
python tools/manage.py migrate
python tools/manage.py --run-syncdb
python tools/manage.py runserver 0.0.0.0:8001