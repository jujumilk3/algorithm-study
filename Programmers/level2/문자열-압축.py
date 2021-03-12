def solution(s):
    length = []
    result = ""
    for i in range(1, len(s)//2 + 1):
        count = 1
        string = s[:i]
        for j in range(i, len(s), i):
            if s[j:j+i] == string:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + string
                string = s[j:j+i]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + string
        length.append(len(result))
        result = ""
    return min(length)


"""
https://velog.io/@devjuun_s/%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4python2020-Kakao-%EA%B3%B5%EC%B1%84
예전에 실제로 저 챌린지(2020 KAKAO BLIND RECRUITMENT)에 참여하기도 했고 나를 오랫동안 괴롭혔던 문제이기도 하다.
처음엔 문제 이해가 어려웠고, 두번째는 제일 앞부터 정해진 길이만큼 잘라야 한다는 조건을 알지 못해서 해맸다.
특히 제일 앞부터 정해진 길이만큼 잘라야 한다는 조건이 문제 설명이나 제한사항에 적혀있지 않고 입출력 에 맨 마지막에나 나와있었기 때문에...
문제를 잘 살펴보지 않는 나쁜 버릇을 가진 내게 치명적으로 다가왔다. 저 조건을 몰랐기 때문에
첫번째 예를 들면 aabbaccc가 있으면 aa, ab, bb, ba, ac, cc 이런 식으로 step을 띄우는 게 아니라 정해진 범위만큼 한칸씩 조사해가며
문자열을 압축시켰기 때문에 구현도 힘들고 답도 틀렸었다. 그래서 이 문제는 정말 몇날 며칠을 고민했었지만 결국 풀지 못했다.
아예 문제를 풀고 자시고 아예 몰랐다고 하는 게 맞을 것이다. 그래서 그냥 다른 풀이를 복붙했다. 그리고 그 코드를 하나하나 뜯어보고
진행해가며 문제를 이해했다. 정말 한심하기 그지없다.
코드의 풀이는 다음과 같다. 처음 for문에서 글자의 단위를 정하고, 단위로 글자를 잘라서 각각 그 글자를 기준으로 똑같은 글자를 찾고,
찾은 수만큼 그 글자와 숫자를 붙여서 새로운 문자열을 만든 다음에 해당 문자열의 길이를 length에 담고, 그 중 가장 짧은 걸 리턴해준다.
나에게는 뭔가 아픈 문제이다.
"""


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
