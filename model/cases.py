import pandas as pd


def cases(df):
    df_formatted = df[['date', 'rolling_average_cases_per_100k_centered', 'state', 'name', 'fipscode']].rename(
        columns={
            'date': 'report_date',
            'rolling_average_cases_per_100k_centered': 'rolling_average_cases_per_100k',
            'state': 'state',
            'name': 'county_name',
            'fipscode': 'fipscode'
        })

    return df_formatted
