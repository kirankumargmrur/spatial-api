# Countries Spatial API
## Project Goal
```
1.Download the world countries geojson data (https://datahub.io/core/geo-countries#resource-geo-countries_zip)
2.Create REST API for that data. 
3.Test CRUD operations for a country. (Delete a country by name, insert new country)
4.Test spatial and non spatial query
  a. Non spatial query :  Get all matching country names by string
  b. Spatial query: Get all counties Intersecting with India
```

## Requirements
```
1.The solution needs to be implemented in Python, preferably 3.x
2.Please use multiple docker containers for the application.
    Ex: One container for Django APP, One for database. 
3.Please use docker-compose to run the application. 
4.Code and commit messages should be treated as you would on a real- world task
5.Please take some time to think about code quality and testing
6.Provide a README with instructions on how to set up, run and test the application
```

## How to <i>Setup</i>
 - Follow the instructions on [docker website](https://docs.docker.com/engine/install/) to install docker on your system.
 - Install docker compose - https://docs.docker.com/compose/install/
 - Clone the repository and navigate inside it
 - Create `.env` file.
 
   Example:
    ```
    DB_NAME='pixxel'
    DB_USER='postgres'
    DB_PASSWORD='wDnfWovh4uf3'
    DB_HOST='db'
    ```
    
      You can copy and paste the above contents to `.env` file and replace APIKEY_1,APIKEY_2,...,APIKEY_N with your Google api keys. 
      And also replace DB_PASSWORD value, you can refer `POSTGRES_PASSWORD` in [docker-compose.yml](/docker-compose.yml) for database password
  
 - Finally run `docker-compose up -d --build` from your terminal

The application will come up @http://localhost:8000 for GeoDjango and @http://localhost:5000 for pygeoapi

## API Description

### PYGEOAPI Server API Reference:
PygeoAPI server can be called at @http://localhost:5000
  - [/collections/countries/items](http://localhost:5000/collections/countries/items)
      - Retrive the list of all the countries


  - [/collections/countries/items/{id}](http://localhost:5000/collections/countries/items/{id})
      - Retrive Country which matches the id


  - [/collections/countries/items?name={name} OR ?id={id} OR ?country_code={country_code}](http://localhost:5000/collections/countries/items?name={name} OR ?id={id} OR ?country_code={country_code})
      - Retrive Country which matches the query passed through the URL


  - [/collections/countries/create](http://localhost:5000/collections/countries/create)
      - REST API to create an entry in the database with data provided


  - [/collections/countries/update](http://localhost:5000/collections/countries/update)
      - POST REST API to update the existing entry in the database with data provided


  - [/collections/countries/delete/{id}](http://localhost:5000/collections/countries/delete/{id})
      - DELETE REST API to  delete the existing entry in the database with id passed in the url ({id} - id of the entry to be deleted)

 - [/collections/countries/intersect/{COUNTRY_NAME}](http://localhost:5000/collections/intersect/{COUNTRY_NAME})
    - Give the list and view of the intersection for the COUNTRY_NAME. Replace the COUNTRY_NAME with exact country name

### Geo Django Server API Reference:
After successful run of docker compose django app is exposed @http://localhost:8000 through gunicorn
 
  - [create/](http://localhost:8000/create/)
     - REST API to create an entry in the database with data provided  
  - [countries/](http://localhost:8000/countries/)
     - Retrive the list of all the countries with Pagination.
     
  - [countries/<int:pk>/](http://localhost:8000/countries/<int:pk>/)
     - Retrive Country which matches the id. Here pk=id of the entry in database
    
  - [update/<int:pk>/](http://localhost:8000update/<int:pk>/)
     - POST REST API to update the existing entry in the database with id provided

  - [delete/<int:pk>/](http://localhost:8000/delete/<int:pk>/)
      - DELETE REST API to  delete the existing entry in the database with id passed in the url ({id} - id of the entry to be deleted)

  - [india/intersection/](http://localhost:8000/india/intersection/)
      - Give the list of the countries that are intersecting with INDIA

  - [spatial/intersection?country={COUNTRY_NAME}](http://localhost:8000/spatial/intersection?country={COUNTRY_NAME})
      - Give the list and view of the intersection for the COUNTRY_NAME. Replace the COUNTRY_NAME with exact country name

 

### Reference
[PyGeoApi](https://docs.pygeoapi.io/en/latest/)

[Django](https://docs.djangoproject.com/en/3.2/)
[GeoDjango](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/)


 
