result_mapper = {
    0: 'E',
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
}
sticks = [input() for x in range(3)]
for stick in sticks:
    print(result_mapper[stick.split().count('0')])
