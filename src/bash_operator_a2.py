from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'kesavan',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}

with DAG(
        dag_id='bash_operator_A2',
        default_args=default_args,
        description='creating a bash operator dag',
        start_date=datetime(2024, 5, 7, 2),
        schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo this is the first task!"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo this is second task!!"
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo this is third task"
    )
    task4 = BashOperator(
        task_id='calculate_square',
        bash_command='expr 5 \* 5'  # Calculate the square of 5
    )

task1>>[task2,task3,task4]
