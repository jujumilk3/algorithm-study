def solution(q, r, code):
    answer = ""
    for i, char in enumerate(code):
        if i % q == r:
            answer += char
    return answer
