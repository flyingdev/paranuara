#!/bin/bash

set -e

while ! (timeout 3 bash -c "</dev/tcp/${DB_HOST}/${DB_PORT}") &> /dev/null;
do
    echo waiting for PostgreSQL to start...;
    sleep 3;
done;

#ping 8.8.8.8

./manage.py makemigrations --merge  --no-input --traceback
./manage.py migrate  --no-input --traceback
if [ $DEBUG == '1' ]
then
   ./manage.py runserver 0.0.0.0:8000
else
   gunicorn -c docker/gunicorn_settings.py paranuara.wsgi --log-config docker/logging.conf
fi