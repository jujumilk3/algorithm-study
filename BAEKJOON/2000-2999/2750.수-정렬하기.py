array_size = int(input())
array = list()
for i in range(array_size):
    array.append(int(input()))
array.sort()
for i in array:
    print(i)
