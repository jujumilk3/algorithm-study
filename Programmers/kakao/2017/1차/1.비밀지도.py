# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append(format(i | j, 'b').zfill(n).replace('1', '#').replace('0', ' '))
    return answer


testcase1 = [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]]
testcase2 = [6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]]


print(solution(*testcase1))
print(solution(*testcase2))






