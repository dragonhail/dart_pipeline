from airflow import DAG
from airflow.contrib.operators.dataproc_operator import DataProcPySparkOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

#producer

# 기본 인수 설정
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'orientation': 'LR', # DAG direction
    'catchup': False
}

dag = DAG(
    'dataproc_pyspark_and_dbt_example',
    default_args=default_args,
    description='A DAG to run PySpark job on Dataproc and dbt run',
    schedule_interval=timedelta(days=1),  # DAG period: everyday
    start_date=days_ago(1),  # DAG start date
    tags=['dataproc', 'pyspark', 'dbt']  # DAG tag
)

run_pyspark_job = DataProcPySparkOperator(
    task_id='run_pyspark_job',
    main='',  # Cloud Storage의 PySpark job 스크립트 경로
    cluster_name='existing-dataproc-cluster',
    region='asia-northeast3',
    dataproc_pyspark_python_version='3',  # Python 버전 (선택적)
    dag=dag
)

# Task: execute dbt 
run_dbt = BashOperator(
    task_id='run_dbt',
    bash_command='dbt run',
    dag=dag
)

# Task Dependency
run_pyspark_job >> run_dbt