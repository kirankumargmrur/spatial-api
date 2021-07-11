#!/bin/bash
set +x

DIR=/app/pygeoapi

cd $DIR
sleep 45
pip install pygeoapi
pip install -r requirements.txt
python setup.py install
export PYGEOAPI_CONFIG=/app/pygeoapi/example-config.yml
export PYGEOAPI_OPENAPI=/app/pygeoapi/example-openapi.yml
pygeoapi generate-openapi-document -c $PYGEOAPI_CONFIG > $PYGEOAPI_OPENAPI
gunicorn pygeoapi.flask_app:APP --bind 0.0.0.0:5000
