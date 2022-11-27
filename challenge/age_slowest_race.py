# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
import datetime
import re
import math


def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
        print(content)
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    date_of_event = datetime.datetime.strptime(re.findall(r'\d{2} \w{3} \d{4}', line)[0], '%d %b %Y')
    date_of_birth = datetime.datetime.strptime(re.findall(r'\d{2} \w{3} \d{4}', line)[1], '%d %b %Y')
    age = (date_of_event - date_of_birth).days / 365.25
    race_time = re.findall(r'\S+', line.strip(' '))[0]
    return (age, race_time)


def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    all_rhines_event_time_and_age = []

    def format_answer(slowest_race):
        age = math.modf(slowest_race[0])
        formated_age = str(int(age[1])) + 'y' + str(round(age[0]*365.25)) + 'd'
        return (formated_age, slowest_race[1])

    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
            all_rhines_event_time_and_age.append(get_event_time(line))

    slowest_race = max(all_rhines_event_time_and_age, key = lambda x: x[1])
    return format_answer(slowest_race)


