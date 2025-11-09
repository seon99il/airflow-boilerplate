from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    dag_id="hello_world",
    start_date=datetime(2024, 1, 1),
    schedule="0 12 * * *",
    catchup=False,
) as dag:


    hello_task = PythonOperator(
        task_id='print_hello',
        python_callable=lambda: print("Hello, World!"),
)