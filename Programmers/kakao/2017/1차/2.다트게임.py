# https://programmers.co.kr/learn/courses/30/lessons/17682


import re


def solution(dart_result):
    shot = re.findall(r'\d{1,2}[SDT][*#]?', dart_result)
    opt = [1, 1, 1]
    for i, s in enumerate(shot):
        if s[-1] == '#':
            opt[i] *= -1
            shot[i] = shot[i][:-1]
        elif s[-1] == '*':
            opt[i] *= 2
            shot[i] = shot[i][:-1]
            if i:
                opt[i - 1] *= 2
    point = [(int(s[:-1]) ** '0SDT'.find(s[-1]) * o) for s, o in zip(shot, opt)]
    return sum(point)


testcase1 = '1S2D*3T'
testcase2 = '1D2S#10S'
testcase3 = '1D2S0T'
testcase4 = '1S*2T*3S'
testcase5 = '1D#2S*3S'
testcase6 = '1T2D3D#'
testcase7 = '1D2S3T*'


print(solution(*testcase1))
print(solution(*testcase2))






