from tracemalloc import start
from airflow.decorators import task, dag
from airflow.providers.docker.operators.docker import DockerOperator
# from docker.types import Mount

from datetime import datetime

@dag(start_date=datetime(2021, 1, 1), schedule_interval='@daily', catchup=False)
def docker_dag():
    @task()
    def t1():
        pass
    
    t2 = DockerOperator(
        task_id='t2',
        api_version='auto',
        container_name='task_t2',
        # image='python:3.8-slim-buster',
        image='stock_image:v1.1.0',
        # command='echo "command running in the docker container"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge', # host - share the same network
        command="python3 stock_data.py",
        retrieve_output=True,
        retrieve_output_path='/tmp/script.out',
        xcom_all=True,
        # cpus=''
        # mem_limit='512m'
        auto_remove=True,
        # mount_tmp_dir=False,
        # mounts=[
        #     Mount(source='/Users/marclamberti/sandbox/includes/scripts', target='/tmp/scripts', type='bind')
        # ]
    )
    
    t1() >> t2

dag = docker_dag()