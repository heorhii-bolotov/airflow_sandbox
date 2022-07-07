from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag_operator import SubDagOperator

from subdags.subdag_parallel_dag import subdag_parallel_dag
from utils.defaults import default_args

from datetime import datetime
 
with DAG(
    'parallel_dag', 
    start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', 
    catchup=False, 
    default_args=default_args
) as dag:
 
    extract_a = BashOperator(
        task_id='extract_a',
        bash_command='sleep 1'
    )
 
    extract_b = BashOperator(
        task_id='extract_b',
        bash_command='sleep 1'
    )
    
    processing = SubDagOperator(
        task_id='processing_tasks',
        subdag=subdag_parallel_dag(
            'parallel_dag',
            'processing_tasks',
            {
                **default_args,
                'start_date': datetime(2022, 1, 1)
            }
        )
    )
 
    transform = BashOperator(
        task_id='transform',
        bash_command='sleep 1'
    )
 
    [extract_a, extract_b] >> processing >> transform
