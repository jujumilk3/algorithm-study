count = int(input())
string_list = []
for i in range(count):
    string_list.append(input())
result = count
for string in string_list:
    used_char_set = set()
    stacked = ''
    ex_char = ''
    for char in string:
        if ex_char and (ex_char != char and char in used_char_set) and char in stacked:
            result -= 1
            break
        ex_char = char
        used_char_set.add(char)
        stacked += char
print(result)

