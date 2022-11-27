# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhines_time = []

    def rhines_time_func(line):
        return re.findall(r'\S+', line.strip(' '))[0]

    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
            rhines_time.append(rhines_time_func(line))

    return rhines_time


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()
    for time in racetimes:
        try:
            time = time.replace('.', ':')
            minutes, seconds, milliseconds = time.split(':')
            total += datetime.timedelta(minutes=int(minutes), seconds=int(seconds), milliseconds=int(milliseconds))
        except:
            minutes, seconds = time.split(':')
            total += datetime.timedelta(minutes=int(minutes), seconds=int(seconds))

        avg_time = f'{total/len(racetimes)}'[2:-5]

    return avg_time
