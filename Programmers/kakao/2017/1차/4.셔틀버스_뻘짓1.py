# https://programmers.co.kr/learn/courses/30/lessons/17678


from datetime import time, timedelta, datetime, date


def solution(run_count, term_minute, capacity, timetable):
    answer = ''
    crew_count = len(timetable)
    print(crew_count)
    return answer


test_time = time(8, 30)
minutes_time_delta = timedelta(minutes=10)
print(test_time)
print(type(test_time))
test_time_str = time(8, 30).strftime('%H:%M')
print(test_time_str)
print(type(test_time_str))

datetime_test = datetime.combine(date.today(), time(8, 30))
print(datetime_test)
print(type(datetime_test))
datetime_test_delta_test = datetime_test + minutes_time_delta
print(datetime_test_delta_test)
print(datetime_test_delta_test.strftime('%H:%M'))

# 이거 말고 분으로 치환하여 구하는 게 더 좋은 방법 같다.


testcase1 = [1, 1, 5, ['08:00', '08:01', '08:02', '08:03']]
testcase2 = [2, 10, 2, ['09:10', '09:09', '08:00']]
testcase3 = [2, 1, 2, ['09:00', '09:00', '09:00', '09:00']]
testcase4 = [1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01']]
testcase5 = [1, 1, 1, ['23:59']]
testcase6 = [10, 60, 45,
             ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59',
              '23:59', '23:59', '23:59', '23:59', '23:59']]

print(solution(*testcase1))
print(solution(*testcase2))
print(solution(*testcase3))
print(solution(*testcase4))
print(solution(*testcase5))
print(solution(*testcase6))
