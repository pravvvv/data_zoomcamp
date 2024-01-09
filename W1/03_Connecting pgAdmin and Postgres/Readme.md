* Access postgres through pgadmin

* Objective is to create a network between 2 docker images :
    * Image : Pull image for PGAdmin
    * Image : Postgres image with ny_taxi database

* First create a docker network
```bash
$ docker network create pg-network
```

* Run the docker image with the ny_taxi db
```bash
$ docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v ~/Documents/GitHub/data_zoomcamp/W1/02_Data_Ingestion_NYC/Data/nyc_data:/var/lib/postgresql/data \
-p 5432:5432 \
--network=pg-network \
--name pg-database \
postgres:13
```

* Run the docker image for PGADMIN
```bash
$ docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
--network=pg-network \
--name pg-admin \
dpage/pgadmin4
```

* Goto http://localhost:8080/
* Click on Servers and Add new Server
* Goto General -- Give a name
* Goto Connection -- username : root, password : root, hostname : pg-database

* Now you will have access to the PGAdmin configured to explore ny_taxi db 