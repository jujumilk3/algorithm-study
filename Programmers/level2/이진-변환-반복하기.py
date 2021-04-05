def solution(s):
    found_zero = 0
    calc_count = 0
    while s != '1':
        calc_count += 1
        new_s = ''
        for char in s:
            if char == '0':
                found_zero += 1
            else:
                new_s += '1'
        s = str(bin(len(new_s)))[2:]
    return [calc_count, found_zero]


print(solution("0111010"))
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
