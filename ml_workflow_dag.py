from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def data_ingestion():
    print("Data ingestion complete")

def data_preprocessing():
    print("Data preprocessing complete")

def model_training():
    print("Model training complete")

def model_evaluation():
    print("Model evaluation complete")

def model_deployment():
    print("Model deployment complete")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
with DAG('ml_workflow_dag', default_args=default_args,
         schedule_interval='@daily', catchup=False) as dag:

    ingestion_task = PythonOperator(
        task_id='data_ingestion',
        python_callable=data_ingestion,
    )

    preprocessing_task = PythonOperator(
        task_id='data_preprocessing',
        python_callable=data_preprocessing,
    )

    training_task = PythonOperator(
        task_id='model_training',
        python_callable=model_training,
    )

    evaluation_task = PythonOperator(
        task_id='model_evaluation',
        python_callable=model_evaluation,
    )

    deployment_task = PythonOperator(
        task_id='model_deployment',
        python_callable=model_deployment,
    )

    ingestion_task >> preprocessing_task >> training_task >> evaluation_task >> deployment_task
