from airflow import DAG
from pendulum import datetime

from core.operators.domain import DomainDockerOperator

with DAG(
        dag_id="sample_dag",
        schedule="@daily",
        start_date=datetime(2023, 1, 1),
        catchup=False,
) as dag:
    DomainDockerOperator(
        task_id="print_meta",
        script="printer.py",
        fn_name="print_meta",
    ) >> DomainDockerOperator(
        task_id="print_meta",
        script="printer.py",
        fn_name="print_meta",
    ) >> DomainDockerOperator(
        task_id="print_meta",
        script="printer.py",
        fn_name="print_meta",
    )
