case_count = int(input())

for i in range(1, case_count + 1):
    string = input()
    palindrome = 1
    for index, char in enumerate(string):
        if char != string[-(index+1)]:
            palindrome = 0
    print('#{} {}'.format(i, palindrome))
