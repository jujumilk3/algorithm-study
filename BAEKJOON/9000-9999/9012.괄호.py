test_case_count = int(input())
parenthesis_list = []

for i in range(test_case_count):
    parenthesis_list.append(input())

for i in range(len(parenthesis_list)):
    temporary_parenthesis_validation_checker = []
    result = ''
    for current_parenthesis in parenthesis_list[i]:
        if current_parenthesis == '(':
            temporary_parenthesis_validation_checker.append(current_parenthesis)
        elif current_parenthesis == ')' and '(' in temporary_parenthesis_validation_checker:
            temporary_parenthesis_validation_checker.remove('(')
        else:
            temporary_parenthesis_validation_checker.append(current_parenthesis)
    result = 'YES' if not temporary_parenthesis_validation_checker else 'NO'
    print(result)

