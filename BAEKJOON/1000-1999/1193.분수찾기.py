find = int(input())

count = 0
number = find

for i in range(1, find+1):
    if find - i > 0:
        find -= i
        count = i
    else:
        break
a = 1 + (find-1)
b = (count+1) - (find-1)

if count % 2 != 0:
    print(str(a)+'/'+str(b))
else:
    print(str(b)+'/'+str(a))
