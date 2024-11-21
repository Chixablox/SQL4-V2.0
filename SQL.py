import pandas as pd
from sqlalchemy import create_engine
df = pd.read_excel('music.xlsx', sheet_name="Лист1")

df['Weekday'] = pd.to_datetime(df['Weekday']).dt.dayofweek

dict_cond = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    0 : 'Sunday'
}

print(df.head(10))

df['Weekday'] = df['Weekday'].map(dict_cond)

df = df.rename(
    columns ={
        'ID' : 'id',
        '  userID' : 'user_id',
        'Track' : 'track',
        '  City  ' : 'city',
        'Report_date' : 'report_date',
        'Weekday' : 'weekday'
    }
)

engine = create_engine('postgresql://postgres:123qwe@localhost:5432/postgres')
df.to_sql('temptable', engine, if_exists='replace', index = False)