def solution(s):
    answer = ''
    for word in s.split(' '):
        temp_word = ''
        for i in range(len(word)):
            if i % 2:
                temp_word += word[i].lower()
            else:
                temp_word += word[i].upper()
        answer += temp_word
        answer += ' '
    return answer[:-1]


print(solution("try hello world"))
print(solution("why so serious"))
print(solution("test"))
print(solution("what the fuck"))
