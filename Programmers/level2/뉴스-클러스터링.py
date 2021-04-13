def solution(str1, str2):
    str1_pairs = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_pairs = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    inter = set(str1_pairs) & set(str2_pairs)
    union = set(str1_pairs) | set(str2_pairs)
    if not union:
        return 65536
    else:
        inter_sum = sum([min(str1_pairs.count(pair), str2_pairs.count(pair)) for pair in inter])
        union_sum = sum([max(str1_pairs.count(pair), str2_pairs.count(pair)) for pair in union])
        return int((inter_sum / union_sum) * 65536)

"""
문제 지문에서 볼 수 있다시피 중복을 허용하는 다중집합에서의 자카드 유사도를 구하는 것이기 때문에 파이썬에서 제공하는 set 자료형으로
문제의 모든 요구사항에 맞출 수 없다. 그래서 문자열을 2글자씩 자른 요소들을 갖고 있는 list를 먼저 만들고 요리조리 조합하여 답을 구했다.

밑에서 교집합 원소 개수와 차집합 원소 개수를 구하는 로직은 너무 깔끔해서 다른 사람의 로직에서 보고 가져왔다.
"""


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('abc', 'def'))
