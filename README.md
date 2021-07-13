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
    
      You can copy and paste the above contents to `.env` file and replace DB_PASSWORD value, you can refer `POSTGRES_PASSWORD` in [docker-compose.yml](/docker-compose.yml) for database password
  
 - Finally run `docker-compose up -d --build` from your terminal

##### Please wait for a minute for applications to come up. I have intentionally kept 45 seconds delay in order to configure database

The application will come up @http://localhost:8000 for GeoDjango and @http://localhost:5000 for pygeoapi

## API Description

### PYGEOAPI Server API Reference:
PygeoAPI server can be called at @http://localhost:5000
  - [/collections/countries/items](http://localhost:5000/collections/countries/items)
      - Retrive the list of all the countries


  - [/collections/countries/items/{id}](http://localhost:5000/collections/countries/items/100)
      - Retrive Country which matches the id


  - [/collections/countries/items?name={name} OR ?id={id} OR ?country_code={country_code}](http://localhost:5000/collections/countries/items?name={name} OR ?id={id} OR ?country_code={country_code})
      - Retrive Country which matches the query passed through the URL


  - [/collections/countries/create](http://localhost:5000/collections/countries/create)
      - REST API to create an entry in the database with data provided


  - [/collections/countries/update](http://localhost:5000/collections/countries/update)
      - POST REST API to update the existing entry in the database with data provided


  - [/collections/countries/delete/{id}](http://localhost:5000/collections/countries/delete/{id})
      - DELETE REST API to  delete the existing entry in the database with id passed in the url ({id} - id of the entry to be deleted)

 - [/collections/countries/intersect/{COUNTRY_NAME}](http://localhost:5000/collectionscountries/intersect/{COUNTRY_NAME})
    - Give the list and view of the intersection for the COUNTRY_NAME. Replace the COUNTRY_NAME with exact country name
    - Example: [INDIA](http://localhost:5000/collections/countries/intersect/India)

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

  - [countries/?q=query_string](http://localhost:8000/countries/?q=query_string)
      -  Get all matching country names by string  

 
## Testing

I have tested application using Postman. Here are few curl requests to  test functionality.

##### To test create api:
```
curl --location --request POST 'http://localhost:5000/collections/countries/create' \
--header 'Content-Type: application/json' \
--data-raw '{ "type": "Feature", "properties": { "name": "Awesome Country", "country_code": "ASM" }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -69.996937628999916, 12.577582098000036 ], [ -69.936390753999945, 12.531724351000051 ], [ -69.924672003999945, 12.519232489000046 ], [ -69.915760870999918, 12.497015692000076 ], [ -69.880197719999842, 12.453558661000045 ], [ -69.876820441999939, 12.427394924000097 ], [ -69.888091600999928, 12.417669989000046 ], [ -69.908802863999938, 12.417792059000107 ], [ -69.930531378999888, 12.425970770000035 ], [ -69.945139126999919, 12.44037506700009 ], [ -69.924672003999945, 12.44037506700009 ], [ -69.924672003999945, 12.447211005000014 ], [ -69.958566860999923, 12.463202216000099 ], [ -70.027658657999922, 12.522935289000088 ], [ -70.048085089999887, 12.531154690000079 ], [ -70.058094855999883, 12.537176825000088 ], [ -70.062408006999874, 12.546820380000057 ], [ -70.060373501999948, 12.556952216000113 ], [ -70.051096157999893, 12.574042059000064 ], [ -70.048736131999931, 12.583726304000024 ], [ -70.052642381999931, 12.600002346000053 ], [ -70.059641079999921, 12.614243882000054 ], [ -70.061105923999975, 12.625392971000068 ], [ -70.048736131999931, 12.632147528000104 ], [ -70.00715084499987, 12.5855166690001 ], [ -69.996937628999916, 12.577582098000036 ] ] ] } }'

```

##### To test Read API

```
curl --location --request GET 'http://localhost:5000/collections/countries/items'
```

##### To test update api:

```
curl --location --request POST 'http://localhost:5000/collections/countries/update' \
--header 'Content-Type: application/json' \
--data-raw '{ "type": "Feature", "properties": { "name": "Pixxel", "country_code": "PIX" }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -69.996937628999916, 12.577582098000036 ], [ -69.936390753999945, 12.531724351000051 ], [ -69.924672003999945, 12.519232489000046 ], [ -69.915760870999918, 12.497015692000076 ], [ -69.880197719999842, 12.453558661000045 ], [ -69.876820441999939, 12.427394924000097 ], [ -69.888091600999928, 12.417669989000046 ], [ -69.908802863999938, 12.417792059000107 ], [ -69.930531378999888, 12.425970770000035 ], [ -69.945139126999919, 12.44037506700009 ], [ -69.924672003999945, 12.44037506700009 ], [ -69.924672003999945, 12.447211005000014 ], [ -69.958566860999923, 12.463202216000099 ], [ -70.027658657999922, 12.522935289000088 ], [ -70.048085089999887, 12.531154690000079 ], [ -70.058094855999883, 12.537176825000088 ], [ -70.062408006999874, 12.546820380000057 ], [ -70.060373501999948, 12.556952216000113 ], [ -70.051096157999893, 12.574042059000064 ], [ -70.048736131999931, 12.583726304000024 ], [ -70.052642381999931, 12.600002346000053 ], [ -70.059641079999921, 12.614243882000054 ], [ -70.061105923999975, 12.625392971000068 ], [ -70.048736131999931, 12.632147528000104 ], [ -70.00715084499987, 12.5855166690001 ], [ -69.996937628999916, 12.577582098000036 ] ] ] } }'
```

##### TO test delete api:

```
curl --location --request DELETE 'http://localhost:5000/collections/countries/delete/101'
```

##### To test Django APIs

  You can directly use the respective api page given by django to post the data or fetch the data.

### Reference
[PyGeoApi](https://docs.pygeoapi.io/en/latest/)

[Django](https://docs.djangoproject.com/en/3.2/)
[GeoDjango](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/)


 
