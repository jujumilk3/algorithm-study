count = int(input())
listed = []
for i in range(count):
    listed.append(input())

for ns in listed:
    number = int(ns.split()[0])
    string = ns.split()[1]
    for char in string:
        print(char * number, end='')
    print()
