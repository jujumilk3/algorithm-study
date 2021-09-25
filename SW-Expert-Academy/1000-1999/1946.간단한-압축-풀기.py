case_count = int(input())

for case_number in range(1, case_count + 1):
    col = int(input())
    string = ''
    for i in range(col):
        input_string = input().split()
        string += input_string[0] * int(input_string[1])
    print('#{}'.format(case_number))
    new_line = 10
    for char in string:
        print(char, end='')
        new_line -= 1
        if new_line == 0:
            new_line = 10
            print()
    print()


"""
1
3
A 10
B 7
C 5 
"""
