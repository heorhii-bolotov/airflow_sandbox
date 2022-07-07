# airflow-first-look

```
make init # open web localhost:8080, login and password "airflow"
docker-compose ps # health check
docker logs materials_name_of_the_container # troubleshoot container

# Restart the container
docker-compose down
docker-compose up -d

# flower localhost:5555/dashboard
```

## Prerequisites

Add .env file before running `docker-compose`

```
AIRFLOW_IMAGE_NAME=apache/airflow:2.3.0
AIRFLOW_UID=1001
AIRFLOW_GID=0
```

## Troubleshoot
* [Denied to write to logs](https://stackoverflow.com/questions/59412917/errno-13-permission-denied-when-airflow-tries-to-write-to-logs)
