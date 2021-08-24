from collections import Counter
word = input().upper()
dicted = sorted(dict(Counter(word)).items(), key=lambda x: x[1], reverse=True)
if len(dicted) > 1 and dicted[0][1] == dicted[1][1]:
    print('?')
else:
    print(dicted[0][0])

