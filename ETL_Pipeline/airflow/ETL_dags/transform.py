import pandas as pd
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values
# Load clean data into postgres database
def task_data_upload(data):
  print(data.head() )
  
  #data = data.to_csv(index=None, header=None)
  file_path = '/Users/ETL_Pipeline/airflow/data.csv'  # Specify the desired file path
  #data.to_csv(file_path, index=None)
  data.to_csv(file_path,index=None,header=None,sep ='\t')#header=None,
  
  return True
  
## perform data cleaning and transformation
def transform_data(df):
  task_data_upload(df)
