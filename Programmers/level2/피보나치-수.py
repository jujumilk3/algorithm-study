def solution(n):
    head = 0
    body = 1
    tail = 1
    for i in range(2, n):
        head = body
        body = tail
        tail = head + body
    return tail


print(solution(3))
print(solution(5))
print(solution(9))
