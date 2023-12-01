import pandas as pd
import gcsfs
from google.cloud import storage

def read_from_cloud():
    storage_client = storage.Client()

    # read data from cloud storage
    bucket = storage_client.bucket('airflow_mini_project_mp')
    blob_t = bucket.blob('data_tsla.csv')
    blob_a = bucket.blob('data_aapl.csv')
    
    # file reader object and store data to df
    with blob_t.open('r') as file_reader:
        df_t = pd.read_csv(file_reader)

    # file reader object and store data to df
    with blob_a.open('r') as file_reader:
        df_a = pd.read_csv(file_reader)

    # union both dataframes
    df_append = pd.concat([df_t,df_a.loc[:]]).reset_index(drop=True)
    print(df_append[df_append['symbol'] == 'TSLA'].head())

read_from_cloud()