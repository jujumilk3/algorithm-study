# https://programmers.co.kr/learn/courses/30/lessons/17677


def solution(str1, str2):
    answer = 0
    str1list = list(str1.lower())
    str2list = list(str2.lower())

    print(str1list)
    print(str2list)
    return answer


testcase1 = ['FRANCE', 'french']
testcase2 = ['handshake', 'shake hands']
testcase3 = ['aa1+aa2', 'AAAA12']
testcase4 = ['E=M*C^2', 'e=m*c^2']


print(solution(*testcase1))
print(solution(*testcase2))
print(solution(*testcase3))
print(solution(*testcase4))


# pseudocode


