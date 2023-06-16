def solution(n):
    answer = []
    x = 2
    while x <= n:
        if n % x == 0:
            if x not in answer:
                answer.append(x)
            n //= x
        else:
            x += 1
    return answer
