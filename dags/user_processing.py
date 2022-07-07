from airflow import DAG
from airflow.operators.bash import BashOperator

import pendulum
import datetime

with DAG(
    dag_id="user_processing",
    schedule_interval="0 0 * * *",
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["custom", "dag1"],
) as dag:

    run_this = BashOperator(
        task_id="run_after_loop",
        bash_command="echo 1",
    )

    run_this

if __name__ == "__main__":
    dag.cli()

# from airflow import DAG

# from datetime import datetime

# with DAG('user_processing', start_date=datetime(2022, 1, 1),
#         schedule_interval='@daily', catchup=False) as dag:
#     None
