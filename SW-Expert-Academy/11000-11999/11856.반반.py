case_count = int(input())

for case_number in range(1, case_count + 1):
    string = input()
    set_string = {*string}
    answer = 'Yes' if len(set_string) == 2 and string.count(string[0]) == 2 else 'No'
    print('#{} {}'.format(case_number, answer))

"""
5
ABAB
CCDD
EFFE
EEEE
NONE 
"""
