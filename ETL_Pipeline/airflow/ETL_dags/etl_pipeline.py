from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
#from datetime import timedelta
from airflow.utils.trigger_rule import TriggerRule
import pandas as pd
from extract import extract_data

def load_data():
    file_path='/Users/ETL_Pipeline/airflow/data.csv'
    postgres_hook = PostgresHook(postgres_conn_id='postgres_connection')
    # Insert the DataFrame into the PostgreSQL database
    postgres_hook.bulk_load('news_etl', file_path)

    return True

def transform_data():
    pass

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 16), # 5-month, 12-date
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


with DAG(
  'etl_news_pipeline',
  default_args=default_args,
  description="A simple news ETL pipeline using Python,PostgreSQL and Apache Airflow",
  start_date=datetime(year=2023, month=5, day=16),
  schedule_interval=timedelta(days=1)
  ) as dag:
  
  start_pipeline = EmptyOperator(
		task_id='start_pipeline',
	)

  extract = BashOperator(
    task_id = 'extract_data',
    bash_command= 'python /Users/ETL_Pipeline/airflow/ETL_dags/extract.py extract_data'
  )

  transform = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
  )

  load = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
  )

  end_pipeline = EmptyOperator(
    task_id='end_pipeline',
  )
  
  start_pipeline >> extract >> transform >> load >> end_pipeline

