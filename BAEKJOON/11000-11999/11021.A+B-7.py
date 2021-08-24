count = int(input())
input_list = []
for i in range(count):
    input_list.append(input())
for index, numbers in enumerate(input_list):
    print("Case #{}:".format(index+1), int(numbers.split()[0]) + int(numbers.split()[1]))
