def solution(n):
    count_one = bin(n).count('1')
    while True:
        n += 1
        if count_one == bin(n).count('1'):
            break
    return n


print(solution(78))
print(solution(15))
