from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import sys
sys.path.insert(0,"/opt/airflow/")
from scripts.get_pokemon_data import run_get_data

import logging
task_logger = logging.getLogger("airflow.task")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'pokemon_data_pipeline',
    default_args=default_args,
    description='Um pipeline simples usando Airflow para obter dados de Pokwmon e salvar em CSV',
    schedule_interval=timedelta(days=1),  # frequencia
)

run_task = PythonOperator(
    task_id='get_data_task',
    python_callable=run_get_data,
    provide_context=True,  # Fornece o contexto para a função
    dag=dag,
)

run_task
