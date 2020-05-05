# https://programmers.co.kr/learn/courses/30/lessons/17677


def solution(str1, str2):
    answer = 0
    str1list = list(str1.lower())
    str2list = list(str2.lower())

    str1_set_list = []
    str2_set_list = []

    for i in range(len(str1list)-1):
        temp_list = [str1list[i], str1list[i+1]]
        str1_set_list.append(temp_list)

    for i in range(len(str2list) - 1):
        temp_list = [str2list[i], str2list[i + 1]]
        str2_set_list.append(temp_list)

    print(str1_set_list)
    print(str2_set_list)

    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))


# strategy
# 일단 모든 문자열을 요소화하고 해당 문자열을 두 개씩 붙여서 새로운 집합을 만든다
#     여기에서 조건이 추가된다. 대소문자 구분이 없고 특수문자는 다음글자로 대체된다.
# 중복을 허용하는 다중집합에서 count(교집합) / count(합집합)이 자카드 유사도가 된다. (1이하)
