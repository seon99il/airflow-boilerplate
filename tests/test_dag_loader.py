import glob
import os
import pytest
from airflow.models import DagBag

DAG_PATH = os.path.join(os.path.dirname(__file__), "../src/dags")
DAG_FILES = glob.glob(DAG_PATH, recursive=True)

@pytest.fixture
def dag_bag():
    return DagBag(dag_folder=DAG_PATH, include_examples=False)


def test_dag_loaded(dag_bag):

    assert dag_bag.import_errors == {}

