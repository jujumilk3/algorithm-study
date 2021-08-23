measures = []
number = int(input())
for i in range(1, number+1):
    if number % i == 0:
        measures.append(i)

for measure in measures:
    print(measure, end=' ')
