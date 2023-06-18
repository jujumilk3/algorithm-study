def solution(picture, k):
    answer = []
    for row in picture:
        line = ""
        for char in row:
            line += char * k
        for i in range(k):
            answer.append(line)
    return answer
