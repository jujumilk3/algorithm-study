# https://programmers.co.kr/learn/courses/30/lessons/17678


def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    for i in range(n):
        last_time = 540 + (n - 1) * t
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        if i == n - 1:
            if timetable[0] > last_time:
                return '%02d:%02d' % (last_time // 60, last_time % 60)
            time = timetable[m - 1] - 1
            return '%02d:%02d' % (time // 60, time % 60)
        for j in range(m - 1, -1, -1):
            bus_arrive = 540 + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]


# 버스의 스케쥴이 나와야 뭐가 된다.
# 이거 말고 분으로 치환하여 구하는 게 더 좋은 방법 같다.
# 제공받은 문자열을 : 기준으로 하여 배열화하고 앞은 0버리고 x60하여 분을 구하고 뒤는 그냥 더해서 총 분으로 구한다

# 소팅해서 먼저온 사람들을 capacity만큼 줄여나간다.

# 전에 했던 거(뻘짓3)는 런타임에러 뜨고 오류 뜨고 난리나는데 이건 멀쩡하게 된다.
# 겉으로 보이는 로직상에 큰 차이는 없는데 어떤 특정한 테스트케이스에서 오류를 뱉게 되는 것 같다.
# 나중에 검사 한번 해보자.


testcase1 = [1, 1, 5, ['08:00', '08:01', '08:02', '08:03']]
testcase2 = [2, 10, 2, ['09:10', '09:09', '08:00']]
testcase3 = [2, 1, 2, ['09:00', '09:00', '09:00', '09:00']]
testcase4 = [1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01']]
testcase5 = [1, 1, 1, ['23:59']]
testcase6 = [10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']]

print(solution(*testcase1))
print()
print(solution(*testcase2))
print()
print(solution(*testcase3))
print()
print(solution(*testcase4))
print()
print(solution(*testcase5))
print()
print(solution(*testcase6))
print()
