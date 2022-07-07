from datetime import datetime, timedelta
import http
import json
from pandas import json_normalize
import logging

from utils.defaults import default_args, tags

from airflow import DAG

# from airflow.providers.postgres.operators import PostgresOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

task_logger = logging.getLogger("airflow.task")


def _process_user(ti):
    user = ti.xcom_pull(task_ids="extract_user")
    task_logger.info(user)
    user = user["results"][0]
    task_logger.info(user)
    processed_user = json_normalize(
        {
            "firstname": user["name"]["first"],
            "lastname": user["name"]["last"],
            "country": user["location"]["country"],
            "username": user["login"]["username"],
            "password": user["login"]["password"],
            "email": user["email"],
        }
    )
    task_logger.info(user)
    processed_user.to_csv("/tmp/processed_user.csv", index=None, header=False)


def _store_user(ti):
    hook = PostgresHook(postgres_conn_id="postgres")
    # hook.bulk_load(
    #     table='users',
    #     tmp_file='/tmp/processed_user.csv'
    # )
    hook.copy_expert(
        sql="COPY users FROM STDIN WITH DELIMITER AS ','",
        filename="/tmp/processed_user.csv",
    )


with DAG(
    dag_id="psql_init_dag",
    start_date=datetime(2022, 7, 7),
    schedule_interval="@once",
    default_args=default_args,
    template_searchpath="/opt/airflow/dags/include",
    tags=[*tags, "dag2"],
    catchup=False,
) as dag:

    create_table = PostgresOperator(
        task_id="create_table", sql="psql_create.sql", postgres_conn_id="postgres"
    )

    is_api_available = HttpSensor(
        task_id="is_api_available", http_conn_id="user_api", endpoint="api/"
    )

    extract_user = SimpleHttpOperator(
        task_id="extract_user",
        http_conn_id="user_api",
        endpoint="api/",
        method="GET",
        response_filter=lambda response: json.loads(response.text),
        log_response=True,
    )

    process_user = PythonOperator(task_id="process_user", python_callable=_process_user)

    store_user = PythonOperator(task_id="store_user", python_callable=_store_user)

    is_api_available >> [create_table, extract_user >> process_user] >> store_user
