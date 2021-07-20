nine_nine_dan_result = {1}

for i in range(1, 10):
    for j in range(1, 10):
        nine_nine_dan_result.add(i * j)

case_count = int(input())
input_numbers = []

for i in range(case_count):
    input_numbers.append(int(input()))

for i in range(case_count):
    print('#{} {}'.format(i+1, 'Yes' if input_numbers[i] in nine_nine_dan_result else 'No'))
