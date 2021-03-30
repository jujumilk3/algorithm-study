def solution(p):
    counter = 0
    inner_counter = 0
    if not p:
        return ''
    u = ''
    v = ''
    for current_p in p:
        if current_p == '(':
            counter += 1
            u += current_p
        else:
            counter -= 1
            u += current_p
        if counter == 0:
            v = p[len(u):]
            u_is_right = True
            for inner_p in u:
                if inner_p == '(':
                    inner_counter += 1
                else:
                    inner_counter -= 1
                if inner_counter < 0:
                    u_is_right = False
            if u_is_right:
                return u + solution(v)
            else:
                new_u = ''
                for i in u[1:-1]:
                    if i == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                answer = '(' + solution(v) + ')' + new_u
                return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution(")))(((()))(("))
print(solution(")()()()("))
