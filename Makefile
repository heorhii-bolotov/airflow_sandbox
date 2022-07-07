
init: docker
	touch .env
	echo 'AIRFLOW_IMAGE_NAME=apache/airflow:2.3.0\nAIRFLOW_UID=1001\nAIRFLOW_GID=0' > .env
	rm -rf ./dags ./logs ./plugins
	mkdir ./dags ./logs ./plugins
	docker compose up -d
	# docker compose exec webserver airflow connections -a --conn_id postgres --conn_uri ssh://user:pass@serverip --conn_extra '{"key_file":"/usr/local/airflow/id_rsa", "no_host_key_check":true}'
	# docker compose exec webserver airflow variables -i variables.json

docker:
	wget -O docker-compose.yaml https://airflow.apache.org/docs/apache-airflow/2.3.0/docker-compose.yaml

up: init
	docker compose up -d

down: 
	docker compose down

it:
	docker exec -it airflow_first_look-airflow-scheduler-1 /bin/bash
	# airflow tasks test psql_init_dag create_table 2022-01-01

psql:
	docker exec -it airflow_first_look-postgres-1 /bin/bash
	psql -Uairflow

cp_cfg:
	docker cp airflow_first_look-airflow-scheduler-1:/opt/airflow/airflow.cfg .

ssh:
	ssh -p 22 airflow@localhost
	airflow webserver
	airflow scheduler