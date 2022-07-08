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

## Notification

[Setup password fot mail app](https://security.google.com/settings/security/apppasswords) - https://security.google.com/settings/security/apppasswords

In airflow.cfg

```
smtp_host = smtp.gmail.com
smtp_user = [your email address] 
smtp_password = [copy from the step before]
smtp_port = 587
smtp_email_from = [your email address] 
```

## Troubleshoot
* [Denied to write to logs](https://stackoverflow.com/questions/59412917/errno-13-permission-denied-when-airflow-tries-to-write-to-logs)
* [Mount sock and change user for running docker operator](https://stackoverflow.com/questions/61186983/airflow-dockeroperator-connect-sock-connectself-unix-socket-filenotfounderror#:~:text=For%20me%20the%20following%20approach%20worked%20to%20get%20it%20run%20on%20my%20local%20machine%3A%20I%20took%20the%20official%20docker%2Dcompose.yaml%20from%20here%3A%20https%3A//github.com/apache/airflow/blob/main/docs/apache%2Dairflow/start/docker%2Dcompose.yaml)
* Elasticsearch - unresolved
