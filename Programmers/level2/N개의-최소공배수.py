from math import gcd


def solution(arr):
    lcm = 0
    for i in range(len(arr)-1):
        head = arr[i] if i == 0 else lcm
        tail = arr[i+1]
        lcm = head * tail // gcd(head, tail)
    return lcm


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
