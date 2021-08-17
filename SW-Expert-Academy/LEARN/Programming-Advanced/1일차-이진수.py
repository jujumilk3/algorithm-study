case_count = int(input())

for i in range(1, case_count + 1):
    num, data = input().split()
    result = ''
    for j in range(int(num)):
        result += '{:04b}'.format(int(data[j], 16))
    print('#{} {}'.format(i, result))
