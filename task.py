import pandas as pd
from model.cases import cases

print('Starting task')
try:
    covid_cases = pd.read_csv(
        'https://raw.githubusercontent.com/biobotanalytics/covid19-wastewater-data/master/cases_by_county.csv')
    cases_MA = covid_cases[covid_cases['state'] == 'MA']
    cases_MA_formatted = cases(cases_MA)
    print(cases_MA_formatted)
except Exception as e:
    print(e)

print('Task complete')