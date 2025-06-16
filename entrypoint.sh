#!/bin/bash
set -e

##
if [ -d "migrations" ]; then
    flask db migrate
    flask db upgrade
else
    flask db init
    flask db migrate
    flask db upgrade
fi

##
exec flask run --host=0.0.0.0 --port=5000