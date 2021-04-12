def convert(n, base):
    arr = '0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, t, m, p):
    answer = ''
    said_number = ''
    number = 0
    while len(said_number) < t * m:
        said_number += convert(number, n)
        number += 1
    said_number = said_number.upper()
    for i in range(p-1, len(said_number), m):
        answer += said_number[i]
        if len(answer) == t:
            break
    return answer
"""
맨 처음에 풀었을땐 로직은 맞았으나 시간초과가 뜨더라. 문제를 잘 보니까 2, 8, 16진수만 있는게 아니라 2 <= n <= 16이었다.
그래서 특정 숫자를 주어진 진수로 바꿔지는 함수를 구해서 썼다...
"""


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
