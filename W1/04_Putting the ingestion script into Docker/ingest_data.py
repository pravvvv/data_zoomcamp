import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    if url.endswith('.parquet.gz'):
        parquet_name = 'output.parquet.gz'
    else:
        parquet_name = 'output.parquet'

    csv_name = 'output.csv'
    # import pandas as pd
    # df = pd.read_parquet('yellow_tripdata_2021-01.parquet')
    # df.to_csv('yellow_tripdata_2021-01.csv',index=False)
    print("url name : ",url)
    os.system(f"wget {url} -O {parquet_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    chunksize = 50000
    
    df = pd.read_parquet(parquet_name)
    df.to_csv(csv_name,index=False)
    df_iter = pd.read_csv(csv_name,iterator=True,chunksize=chunksize)
    df.head(n=0).to_sql(name=table_name,con=engine,if_exists='replace')
    from time import time
    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
            df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
            df.to_sql(name=table_name,con=engine,if_exists='append')
            t_end = time()
            duration = t_end - t_start
            print("Chunk size added : %f, took %.3f " % (len(df),duration) )
            
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest Parquet data to PG')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')


    args = parser.parse_args()


    main(args)
