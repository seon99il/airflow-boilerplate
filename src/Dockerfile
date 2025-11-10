FROM apache/airflow:2.9.1

COPY requirements.txt .
COPY custom-package /opt/airflow/custom-package


RUN pip install --no-cache-dir -r requirements.txt
USER root
RUN chown -R airflow /opt/airflow/custom-package
USER airflow
RUN pip install -e /opt/airflow/custom-package
