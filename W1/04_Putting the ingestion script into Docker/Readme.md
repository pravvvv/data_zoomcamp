* Convert jupyter notebook to python script using
```bash
jupyter nbconvert --to=script Data_Ingestion.ipynb

```

* Modify the script as required (ref. Data_Ingestion.py) in the same folder

* Run the command to run the python file
```bash

$ export url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

python ingest_data.py \
--user=root \
--password=root \
--host=localhost \
--port=5432 \
--db=ny_taxi \
--table_name=yellow_taxi_trips \
--url=$url

```