def solution(intStrs, k, s, l):
    answer = []
    for istr in intStrs:
        if int(istr[s : s + l]) > k:
            answer.append(int(istr[s : s + l]))
    return answer
