number = int(input())
count = 0
triple_sixes = []
progress = 666
while count < number:
    if '666' in str(progress):
        triple_sixes.append(progress)
        count += 1
    progress += 1

print(triple_sixes.pop())



