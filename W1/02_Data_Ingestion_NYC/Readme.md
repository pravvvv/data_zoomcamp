Image :
* Postgres13
* Map a folder to bind volume

* Start the docker container by running the docker command : 
```bash
$ docker run -it \
    -e POSTGRES_USER="root"
    -e POSTGRES_PASSWORD="root"
    -e POSTGRES_DB="ny_taxi"
    -v ny_taxi_postgres_data:/var/lib/postgresql/data
    -p 5432:5432
    postgres:13```
```

