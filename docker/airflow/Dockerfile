FROM apache/airflow:3.1.2-python3.12

USER airflow

RUN --mount=type=bind,source=pyproject.toml,target=/tmp/project/pyproject.toml \
    uv pip install --group /tmp/project/pyproject.toml:airflow
