SELECT *
from {{ref('dags')}} as dag
LEFT JOIN {{ref('task_fail')}} as task_fail  on dag.dag_id = task_fail.dag_id