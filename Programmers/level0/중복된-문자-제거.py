def solution(my_string):
    already = set()
    answer = ""
    for char in my_string:
        if char not in already:
            already.add(char)
            answer += char
    return answer
