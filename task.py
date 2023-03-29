import psycopg2
import pandas as pd
import os
from decouple import config
from sqlalchemy import create_engine
from model.cases import cases

print('Starting task')
db_config = {
    "user": config('username'),
    "password": config('password'),
    "host": config('host'),
    "database": config('database'),
}

try:
    conn_string = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}/{db_config["database"]}'
    db = create_engine(conn_string)
    conn = db.connect()

    covid_cases = pd.read_csv('https://raw.githubusercontent.com/biobotanalytics/covid19-wastewater-data/master/cases_by_county.csv', index_col=[0])
    # cases_MA = covid_cases[covid_cases['state'] == 'MA']
    # cases_MA_formatted = cases(cases_MA)
    print(covid_cases)

    covid_cases.to_sql('daily_cases_average', conn, schema='covid_metrics_raw', if_exists='replace', index=False)

    conn.close()
except Exception as e:
    print(e)

print('Task complete')