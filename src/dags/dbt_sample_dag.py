import os
from datetime import datetime

from cosmos import DbtDag, ExecutionConfig, ProfileConfig, ProjectConfig, RenderConfig
from cosmos.profiles import (
    PostgresUserPasswordProfileMapping,
)

CURRENT = os.path.dirname(os.path.abspath(__file__))
DBT_PROJECT = os.path.join(CURRENT, "dbt/airflow")

execution_config = ExecutionConfig(
    dbt_executable_path="dbt",
)


project_config = ProjectConfig(
    dbt_project_path=DBT_PROJECT,
    install_dbt_deps=True,
)


profile_config = ProfileConfig(
    profile_name="airflow",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_default",
        profile_args={  # Override any default profile parameters here
            "host": "postgres",
            "port": 5432,
            "user": "airflow",
            "password": "airflow",
            "dbname": "airflow",
            "schema": "public",
        },
    ),
)

dbt_sample_dag = DbtDag(
    project_config=project_config,
    profile_config=profile_config,
    execution_config=execution_config,
    schedule_interval="@daily",
    start_date=datetime(2025, 11, 1),
    catchup=False,
    dag_id="dbt_sample_dag",
    render_config=RenderConfig(
        select=["+task_fail_with_dag"],  # select all models dependent on dag_count
    ),
)
