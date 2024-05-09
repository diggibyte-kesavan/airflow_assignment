from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args={
    'owner':'upstream_downstream',
    'retries':5,
    'retry_delay':timedelta(minutes=2)

}

with DAG(
    dag_id='upstream_downstream_A5',
    default_args=default_args,
    description='upstream_downstream_with_dependency',
    start_date=datetime(2024, 5, 9),
    schedule_interval='@daily'
)as dag:
   task1=BashOperator(
    task_id='first_task',
    bash_command="echo this is the first task!"
   )
   task2=BashOperator(
    task_id='second_task',
    bash_command="echo this is second task!"
   )
   task3=BashOperator(
    task_id='third_task',
    bash_command="echo this is third task!"
   )
task1>>task2
task1>>task3
task2>>task3
