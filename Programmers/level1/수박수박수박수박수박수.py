def solution(n):
    water_melon = '수박'
    return water_melon * (n // 2) + water_melon[0] * (n % 2)


print(solution(3))
print(solution(4))