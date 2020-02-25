inputted_number = input().split()
first_number = int(inputted_number[0])
doubled = first_number * 2
summed = sum([int(x) for x in inputted_number])

if doubled == summed:
    print('==')
elif doubled > summed:
    print('>')
else:
    print('<')



