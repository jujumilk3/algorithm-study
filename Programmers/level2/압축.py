dictionary = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def solution(msg):
    answer = []
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dictionary.index(msg[w:c]))
            break
        if msg[w:c+1] not in dictionary:
            dictionary.append(msg[w:c+1])
            answer.append(dictionary.index(msg[w:c]))
            w = c
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
