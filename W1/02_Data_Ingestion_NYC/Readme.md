Image :
* Postgres13
* Map a folder to bind volume

* (Optional) If there is any existing postgres server running please stop the server using the command :
```
$ sudo systemctl stop postgresql
```

* Start the docker container by running the docker command : 
```bash
$ docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v ~/Documents/GitHub/data_zoomcamp/W1/02_Data_Ingestion_NYC/Data/nyc_data:/var/lib/postgresql/data \
-p 5432:5432 \
postgres:13
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

* Download using the command 
```
$ wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
```

# Jupyter notebook

* Go to this directory and create a Jupyter notebook using
```
$ jupyter notebook
```

* Within jupyter notebook use python to convert this to csv as shown
```python
import pandas as pd
df = pd.read_parquet('yellow_tripdata_2021-01.parquet')
df.to_csv('yellow_tripdata_2021-01.csv',index=False)
```

* Use terminal for these commands 
```
$ head -n 5 yellow_tripdata_2021-01.csv # top 5 rows
$ tail -n 5 yellow_tripdata_2021-01.csv # bottom 5 rows
$ head -n 100 yellow_tripdata_2021-01.csv > yellow_head.csv # use output to write to file
$ wc -l yellow_tripdata_2021-01.csv # for word count
```

* Using pgcli use these commands 
    * \dt - List all tables
    * \d <table_name> - DESC table
    

* Using pandas we could break the data into chunks using this code and ingest the csv file to the PG database (Ref. Jupyter file)
```python
from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

chunksize = 50000
df_iter = pd.read_csv('yellow_tripdata_2021-01.csv',iterator=True,chunksize=chunksize)
df.head(n=0).to_sql(name='yellow_taxi_data',con=engine,if_exists='replace')
from time import time
while True:
    try:
        t_start = time()
        df = next(df_iter)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df.to_sql(name='yellow_taxi_data',con=engine,if_exists='append')
        t_end = time()
        duration = t_end - t_start
        print("Chunk size added :",len(df), ", duration :",duration)
        
    except StopIteration:
        print("Iteration over")
        break
```

