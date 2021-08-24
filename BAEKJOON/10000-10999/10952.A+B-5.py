flag = True
while flag:
    inputted_number = input()
    answer = int(inputted_number.split()[0]) + int(inputted_number.split()[1])
    if answer:
        print(answer)
    else:
        flag = False
