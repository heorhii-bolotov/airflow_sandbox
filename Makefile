
init: docker
	touch .env
	echo 'AIRFLOW_IMAGE_NAME=apache/airflow:2.3.0\nAIRFLOW_UID=1001\nAIRFLOW_GID=0' > .env
	rm -rf ./dags ./logs ./plugins
	mkdir ./dags ./logs ./plugins
	docker compose up -d

docker:
	wget -O docker-compose.yaml https://airflow.apache.org/docs/apache-airflow/2.3.0/docker-compose.yaml

up: init
	docker compose up -d

down: 
	docker compose down
