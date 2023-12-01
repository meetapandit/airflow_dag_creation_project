from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import datetime
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from support.extract_data import extract_task_1, extract_task_2
from support.read_data import read_from_cloud

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 30),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
'marketvol',
default_args=default_args,
description='Market Volume DAG',
schedule_interval=None,
)

task1 = PythonOperator(
    task_id='extract_tsla',
    python_callable=extract_task_1,
    dag=dag,
)

task2 = PythonOperator(
    task_id='extract_aapl',
    python_callable=extract_task_2,
    dag=dag,
)

task3 = PythonOperator(
    task_id='read_from_storage',
    python_callable=read_from_cloud,
    dag=dag,
)

[task1, task2] >> task3

