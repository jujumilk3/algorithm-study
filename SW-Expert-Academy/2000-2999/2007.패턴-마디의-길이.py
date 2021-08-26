# case_count = int(input())
#
# for i in range(1, case_count + 1):
#     string = input()
#     word = ''
#     for char in string:
#         word += char
#         length = len(word)
#         if word == string[length:length+length]:
#             break
#     print('#{} {}'.format(i, len(word)))

case_count = int(input())

for i in range(1, case_count + 1):
    string = input()
    word = ''
    for char in string:
        word += char
        length = len(word)
        if word == string[length:length+length]:
            rest_string = string[length:]
            rest_string = rest_string.replace(word, '')
            if len(rest_string) < len(word):
                break
    print('#{} {}'.format(i, len(word)))




"""
7
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY
KKKKKAAAAAKKKKKAAAAAKKKKKAAAAA
MMORPGMMORPGMMORPGMMORPGMMORPG
ABCDEFGHUJKLMNOPQRSTUVWXYZWLWM
SAMSUNGSAMSUNGSAMSUNGSAMSUNGZZ
"""
