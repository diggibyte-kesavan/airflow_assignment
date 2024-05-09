from airflow.sensors.filesystem import FileSensor
from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'file_sensor',
    'retries': 1,
    'retries_delay': 3,
}
with DAG(
        default_args=default_args,
        dag_id="file_sensor_A6",
        start_date=datetime(2024, 5, 9),
        catchup=False,
        schedule_interval='@daily'
) as dag:
    wait_for_file = FileSensor(task_id="file_sensor",
                               fs_conn_id='wait_for_file',
                               filepath='customer.py',
                               mode='reschedule',
                               poke_interval=30)