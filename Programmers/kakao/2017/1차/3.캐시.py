# https://programmers.co.kr/learn/courses/30/lessons/17680


def solution(cache_size, cities):
    time = 0
    cache_array = [' '] * cache_size

    for city in cities:
        city_lowered = city.lower()
        if city_lowered in cache_array:
            time = time + 1
            cache_array.remove(city_lowered)
            cache_array.append(city_lowered)
        else:
            time += 5
            cache_array.append(city_lowered)
            cache_array.pop(0)
    return time


testcase1 = (3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])
testcase2 = (3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'])
testcase3 = (2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'])
testcase4 = (5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'])
testcase5 = (2, ['Jeju', 'Pangyo', 'NewYork', 'newyork'])
testcase6 = (0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])

print(solution(*testcase1))
print(solution(*testcase2))
print(solution(*testcase3))
print(solution(*testcase4))
print(solution(*testcase5))
print(solution(*testcase6))
