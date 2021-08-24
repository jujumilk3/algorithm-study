first_number = int(input())
second_number = 0
result_number = 0
roof_counter = 1

if not 0 <= first_number <= 99:
    exit()

number_checker = first_number

while True:
    second_number = first_number % 10
    first_number = int(first_number / 10)
    result_number = first_number + second_number
    first_number = (second_number * 10) + result_number % 10

    if number_checker == first_number:
        break
    else:
        roof_counter += 1

print(roof_counter)
