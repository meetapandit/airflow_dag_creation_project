import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import gcsfs
from google.cloud import storage

'''
    Input: Download stock data for previous day from Yahoo finance

    Output: Store the downloaded data to cloud storage

'''
def extract_task_1():
    storage_client = storage.Client()
    # column_list = ['date', 'open', 'high', 'low', 'close', 'adj close', 'volume']
    start_date = datetime.today() - timedelta(days=1)
    end_date = start_date + timedelta(days=1)
    print("download stock data")
    tsla_df = yf.download('TSLA', start=start_date, end=end_date, interval='1m')
    tsla_df['symbol'] = 'TSLA'
    bucket = storage_client.bucket('airflow_mini_project_mp')
    blob = bucket.blob('data_tsla.csv')
    print("write data to cloud storage")
    with blob.open('w') as file_writer:
        tsla_df.to_csv(file_writer, header=True)
    return

def extract_task_2():
    storage_client = storage.Client()
    # column_list = ['date', 'open', 'high', 'low', 'close', 'adj close', 'volume']
    start_date = datetime.today() - timedelta(days=1)
    end_date = start_date + timedelta(days=1)
    print("download stock data")
    tsla_df = yf.download('AAPL', start=start_date, end=end_date, interval='1m')
    tsla_df['symbol'] = 'AAPL'
    bucket = storage_client.bucket('airflow_mini_project_mp')
    print("write data to cloud storage")
    blob = bucket.blob('data_aapl.csv')
    with blob.open('w') as file_writer:
        tsla_df.to_csv(file_writer, header=True)
    return

extract_task_1()
extract_task_2()