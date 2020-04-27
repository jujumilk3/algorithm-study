def solution(arrangement):
    answer = 0
    current_open_bracket = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            current_open_bracket += 1
        else:
            if arrangement[i - 1] == '(':
                current_open_bracket -= 1
                answer += current_open_bracket
            else:
                current_open_bracket -= 1
                answer += 1
    return answer


print(solution("()"))
print('#' * 50)
print(solution("(())"))
print('#' * 50)
print(solution("(((()())))"))
print('#' * 50)
print(solution("(((()())(())()))"))
print('#' * 50)
print(solution("()(((()())(())()))(())"))
print('#' * 50)
print(solution("((()())(())())"))

