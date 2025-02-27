#!/bin/sh

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=config.settings config.wsgi:application --bind 0.0.0.0:$PORT