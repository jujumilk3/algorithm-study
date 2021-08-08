def solution(s):
    answer = []
    as_lists = s[2:-2].split('},{')
    as_lists.sort(key=len)
    for as_string_list in as_lists:
        as_list = as_string_list.split(',')
        for number in as_list:
            integer = int(number)
            if integer not in answer:
                answer.append(integer)
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
