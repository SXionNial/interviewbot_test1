#!/usr/bin/env bash

set -o errexit  # exit on error

heroku run pip install -r requirements.txt

heroku config:set DISABLE_COLLECTSTATIC=1
heroku run python manage.py migrate
heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'
heroku config:unset DISABLE_COLLECTSTATIC
heroku run python manage.py collectstatic