hands = input().split()
result = ''

if hands[0] == '1' and hands[1] == '2':
    result = 'B'
elif hands[0] == '1' and hands[1] == '3':
    result = 'A'
elif hands[0] == '2' and hands[1] == '1':
    result = 'B'
elif hands[0] == '2' and hands[1] == '3':
    result = 'A'
elif hands[0] == '3' and hands[1] == '1':
    result = 'B'
elif hands[0] == '3' and hands[1] == '2':
    result = 'A'

print(result)
