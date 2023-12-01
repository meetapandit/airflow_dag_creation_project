# Stock Market DAG creation in Airflow on GCP

### Overview
- The goal of this mini project was to create dags using PythonOperator and scehduling task dependencies in Airflow
- To achieve this extracted stock market data from Yahoo finance API and uploaded to GCP by creating workflows in Airflow

### Workflow Details
- Extract daily stock market data with 1min intervals and create 2 Python functions for this step
- Save the csv files to Google Cloud Storage bucket using gcloud client for Python
- Create 3rd task for reading the data from Cloud storage and filtering the required stock market symbol from the data and displaying it to console
- The tasks 'extract_tsla' and 'extract_aapl' run in parallel and 'read_from_storage' starts only after the first 2 extraction tasks are completed

### Airflow UI showing workflow details

<img width="1183" alt="Screenshot 2023-12-01 at 3 04 57 PM" src="https://github.com/meetapandit/airflow_dag_creation_project/assets/15186489/ed08a9cb-418b-4815-83f7-5330a937ff7a">

- The left navigation tab shows that the DAG ran successfully on the 2nd run
- The following image shows the output of the data read from GCP to the console which shows that the dag ran successfully

<img width="1406" alt="Screenshot 2023-12-01 at 3 09 21 PM" src="https://github.com/meetapandit/airflow_dag_creation_project/assets/15186489/eebcd96f-e61d-4495-9591-a02f9d8803b7">
