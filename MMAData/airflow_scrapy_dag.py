from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
        'owner': 'airflow',
        'start_date': datetime(2021, 7, 24)
        }

dag = DAG('scrapy_crawler', default_args=default_args, catchup=False)

t1 = BashOperator(
    task_id='delete_fighter',
    bash_command="""cd /c/Users/ccsuc/Desktop/UFCScraper && rm fighter.json""",
    dag=dag)

t2 = BashOperator(
    task_id='schedule_scrapy_crawler',
    bash_command="""cd /c/Users/ccsuc/Desktop/UFCScraper && scrapy crawl fighter_scraper -o fighter.json""",
    dag=dag)

t3 = BashOperator(
    task_id='schedule_pandas_cleaner',
    bash_command="""cd /c/Users/ccsuc/Desktop/UFCScraper && python3 fighter_data_cleaner.py""",
    dag=dag)


t1 >> t2 >> t3