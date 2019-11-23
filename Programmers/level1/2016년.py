import datetime


def solution(a, b):
    day_of_the_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return day_of_the_week[datetime.datetime(2016, a, b).weekday()]


print(solution(5, 24))

