def solution(s):
    answer = []
    complete_nums = []
    number = ''
    for char in s:
        if char.isdigit():
            number += char
        elif number:
            if int(number) not in complete_nums:
                complete_nums.append(int(number))
            number = ''
    print(complete_nums)
    return {*complete_nums}


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
