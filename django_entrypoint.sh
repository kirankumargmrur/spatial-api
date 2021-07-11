#!/bin/bash
set +x

APP_NAME=pixxel_test
DIR=/app/
LOG_LEVEL=
MAX_NO_REQUESTS_PER_WORKER=
JITTER=
#Sleep until db comesup
sleep 45
#RUN Migrations
ogr2ogr -f PostgreSQL PG:"host=db user=postgres password=wDnfWovh4uf3 dbname=pixxel" -nlt PROMOTE_TO_MULTI  -lco GEOMETRY_NAME=geometry countries/data/archive/countries.geojson -nln countries -overwrite
PGPASSWORD=wDnfWovh4uf3  psql -U postgres -d pixxel -h db -c "ALTER TABLE countries RENAME ogc_fid TO id;"
PGPASSWORD=wDnfWovh4uf3  psql -U postgres -d pixxel -h db -c "ALTER TABLE countries RENAME admin TO name;"
PGPASSWORD=wDnfWovh4uf3  psql -U postgres -d pixxel -h db -c "ALTER TABLE countries RENAME iso_a3 TO country_code ;"
PGPASSWORD=wDnfWovh4uf3  psql -U postgres -d pixxel -h db -c "ALTER TABLE countries RENAME wkb_geometry TO geometry ;"
python3 manage.py makemigrations countries
python3 manage.py migrate
PGPASSWORD=wDnfWovh4uf3  psql -U postgres -d pixxel -h db -c "ALTER TABLE countries ALTER COLUMN geometry type geometry(MultiPolygon, 4326) using ST_Multi(geometry);"

#Start server as gunicorn
gunicorn pixxel_test.wsgi:application \
      --bind 0.0.0.0:8000 \
      --max-requests 1000 \
      --max-requests-jitter 50 \
      --workers 3 \
      --access-logfile='-' \
      --access-logformat='%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(p)s" "%(D)s"'
