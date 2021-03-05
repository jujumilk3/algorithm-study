def solution(new_id):
    # first filter
    answer = new_id.lower()
    recommend_id = ''
    # second filter
    for char in answer:
        if char.isalnum() or char in '-_.':
            recommend_id += char
    # third filter
    answer = recommend_id
    while '..' in answer:
        answer = answer.replace('..', '.')
    # fourth filter
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # fifth filter
    if not answer:
        answer += 'a'
    # sixth filter
    answer = answer[:15] if len(answer) > 15 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # seventh filter
    while len(answer) < 3:
        answer += answer[-1]
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
