def solution(strings, n):
    answer = []
    for string in strings:
        answer.append(string[n] + string)
    answer.sort()
    answer = [x[1:] for x in answer]
    return answer


print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))
