def solution(myString, pat):
    answer = 0
    len_of_pat = len(pat)
    for i in range(len(myString) - len_of_pat + 1):
        if pat in myString[i : i + len_of_pat]:
            answer += 1
    return answer
