def solution(coordinates):
    answer = []
    first = []
    second = []
    for dot in coordinates:
        first.append(dot[0])
        second.append(dot[1])

    print(first)
    print(second)
    for i in range(3):
        print("카운트는")
        print("현재second는")
        print(second[i])
        print(second.count(second[i]))
        if second.count(second[i]) % 2 != 0:
            answer.append(second[i])
            print("첫번째")
            print(second[i])
        if first.count(first[i]) % 2 != 0:
            answer.append(first[i])
            print(first[i])

    return answer


testcase1 = [[1, 4], [3, 4], [3, 10]]
testcase2 = [[1, 1], [2, 2], [1, 2]]

print(solution(testcase1))
print(solution(testcase2))
