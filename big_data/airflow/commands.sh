## acessar container com o servidor airflow
docker exec -it d91baf104a11 /bin/bash

## rodar task
airflow tasks test pokemon_data_pipeline get_data_task 2022-01-25

## reiniciar servidor airflow
airflow webserver -D

## iniciar dag
airflow dags list
airflow dags trigger pokemon_data_pipeline


## Liga airflow
docker-compose up -d

## reiniciar
docker-compose restart

## Log
docker logs  d91baf104a11

docker restart d91baf104a11