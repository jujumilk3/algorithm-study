def solution(s, n):
    answer = ''
    for character in s:
        current_ord = ord(character)
        applied_ord = ''
        if 64 < current_ord < 91:
            if 90 < current_ord + n:
                applied_ord = 64 + current_ord + n - 90
            else:
                applied_ord = current_ord + n
        elif 96 < current_ord < 123:
            if 122 < current_ord + n:
                applied_ord = 96 + current_ord + n - 122
            else:
                applied_ord = current_ord + n
        else:
            applied_ord = 32
        answer += chr(applied_ord)
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("uUVWAABBz", 13))

