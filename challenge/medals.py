from collections import namedtuple
import pandas as pd

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = pd.read_csv('olympics.txt', sep=";")


def get_query(key, value):
    query = key + ' == "' + value + '" & '
    return query


def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    total_query = ''
    for key, value in kwargs.items():
        query = get_query(key, value)
        total_query += query

    total_query = total_query[:-3]
    df = medals.query(total_query)
    df = df.astype({'Edition': 'str'})
    return list(df.itertuples(name='medal', index=False))

actual = len(get_medals(Edition='1984'))
expected = 1459
print(actual)
print(expected)
print(actual == expected)

