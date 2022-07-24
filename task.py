import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from model.cases import cases

print('Starting task')

try:
    conn_string = 'postgresql://postgres:password@localhost/covid_metrics'
    db = create_engine(conn_string)
    conn = db.connect()

    covid_cases = pd.read_csv('https://raw.githubusercontent.com/biobotanalytics/covid19-wastewater-data/master/cases_by_county.csv')
    cases_MA = covid_cases[covid_cases['state'] == 'MA']
    cases_MA_formatted = cases(cases_MA)

    cases_MA_formatted.to_sql('daily_cases_average', conn, schema='wastewater', if_exists='replace', index=False)

    conn.close()
except Exception as e:
    print(e)

print('Task complete')