from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def fun1():
    print("This is the first task")


def fun2():
    print("This is the second task")


def fun3():
    print("This is the third task")


default_args = {
    'owner': 'kesavan',
    'start_date': datetime(2024, 5, 9),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# define DAG
with DAG(
        'simple_demo_dag_A1',
        default_args=default_args,
        description='DEMO DAG',
        schedule_interval=timedelta(days=1),
) as dag:
    # Define the tasks
    task_1 = PythonOperator(
        task_id='first_task',
        python_callable=fun1,
    )
    task_2 = PythonOperator(
        task_id='second_task',
        python_callable=fun2,
    )

    task_3 = PythonOperator(
        task_id='third_task',
        python_callable=fun3,
    )
    # define the task dependencies
    task_1 >> task_2 >> task_3
