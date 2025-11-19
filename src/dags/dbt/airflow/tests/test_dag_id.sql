-- 결과가 있다면 실패

SELECT COUNT(1) AS cnt
FROM {{ref('dags')}}
WHERE dag_id IS NULL
HAVING COUNT(1) > 0