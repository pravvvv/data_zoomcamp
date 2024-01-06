Image :
* Postgres13
* Map a folder to bind volume

* Start the docker container by running the docker command : 
```bash
$ docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v ny_taxi_postgres_data:/var/lib/postgresql/data -p 5432:5432 postgres:13
```

* To access the postgres in the container use :
```
$ psql -h localhost -p 5432 -U root -d ny_taxi
```
or

```
$ pgcli -h localhost -p 5432 -u root -d ny_taxi
```

# Ingesting data to Postgres

## Dataset source
*  [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

*   [Jan 2021 Yellow taxi](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet )


